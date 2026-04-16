from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from difflib import SequenceMatcher
from importlib import import_module
from pathlib import Path
import re
from typing import Any, Callable, Iterable

from .json_io import ensure_parent_dir, write_json, write_text

OUTPUT_ROOT = Path("output")
DEFAULT_MARKET_ANALYTICS_OUTPUT = OUTPUT_ROOT / "reports" / "market_analytics.json"
DEFAULT_MARKET_ANALYTICS_MARKDOWN_OUTPUT = (
    OUTPUT_ROOT / "reports" / "market_analytics_report.md"
)
DEFAULT_CHARTS_OUTPUT_DIR = OUTPUT_ROOT / "site" / "static" / "charts"
DEFAULT_SITE_ANALYTICS_OUTPUT = OUTPUT_ROOT / "site" / "content" / "analytics.md"

HIGH_CONFIDENCE_SCORE = 0.92

TITLE_GROUP_THRESHOLD = 0.78

TITLE_STOPWORDS = {
    "a",
    "an",
    "and",
    "for",
    "of",
    "the",
    "to",
    "with",
}

SENIORITY_PATTERNS: list[tuple[str, tuple[str, ...]]] = [
    (
        "Leadership",
        (
            "chief",
            "cto",
            "director",
            "head",
            "lead",
            "manager",
            "principal",
            "staff",
            "vp",
        ),
    ),
    ("Senior", ("senior", "specialist", "sr")),
    (
        "Entry",
        ("apprentice", "entry", "graduate", "intern", "junior", "trainee"),
    ),
]

_ANALYTICS_FRONTMATTER = """\
+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "{generated_at}"
last_research_at = "{generated_at}"
+++

"""

SCORE_LABELS: list[tuple[float, str, str]] = [
    (1.00, "exact_normalized", "1.00 exact_normalized"),
    (0.92, "alias_table", "0.92 alias_table"),
    (0.85, "fuzzy_strong", "0.85 fuzzy_strong"),
    (0.50, "recruiter_or_ambiguous", "0.50 recruiter_or_ambiguous"),
    (0.20, "substring_only", "0.20 substring_only"),
]

MATCH_TYPE_PRIORITY = {
    match_type: index for index, (_, match_type, _) in enumerate(SCORE_LABELS)
}


def _coerce_metadata_and_rows(
    matches: Any,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    if isinstance(matches, dict):
        metadata = matches.get("metadata", {})
        rows = matches.get("matches", [])
        if isinstance(metadata, dict) and isinstance(rows, list):
            return metadata, [row for row in rows if isinstance(row, dict)]
        return {}, []

    if isinstance(matches, list):
        return {}, [row for row in matches if isinstance(row, dict)]

    if isinstance(matches, Iterable):
        return {}, [row for row in matches if isinstance(row, dict)]

    return {}, []


def _coerce_dict(value: Any) -> dict[str, Any]:
    """Safely coerce a value to dict, returning empty dict if not a dict."""
    if isinstance(value, dict):
        return value
    return {}


def _coerce_offer(row: dict[str, Any]) -> dict[str, Any]:
    return _coerce_dict(row.get("offer", {}))


def _coerce_match(row: dict[str, Any]) -> dict[str, Any]:
    return _coerce_dict(row.get("match", {}))


def _coerce_sponsor(row: dict[str, Any]) -> dict[str, Any]:
    return _coerce_dict(row.get("sponsor", {}))


def _string_value(value: Any, *, default: str = "Unknown") -> str:
    text = str(value or "").strip()
    return text or default


def _safe_float(value: Any, *, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _safe_int(value: Any, *, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _extract_score(row: dict[str, Any]) -> float:
    nested_match = _coerce_match(row)
    for key in ("score", "match_score", "quality_score"):
        if key in nested_match:
            return _safe_float(nested_match.get(key))
        if key in row:
            return _safe_float(row.get(key))
    return 0.0


def _extract_weight(row: dict[str, Any]) -> float:
    return max(0.0, min(1.0, _extract_score(row)))


def _extract_nested_value(
    row: dict[str, Any],
    nested_key: str,
    field_names: tuple[str, ...],
    converter: Callable[[Any], Any] = lambda x: x,
    default: Any = None,
) -> Any:
    """Extract a field from nested structure or row, with type conversion."""
    nested = _coerce_dict(row.get(nested_key, {}))
    for field in field_names:
        if field in nested:
            return converter(nested.get(field))
        if field in row:
            return converter(row.get(field))
    return default


def _extract_match_type(row: dict[str, Any]) -> str:
    return _extract_nested_value(
        row, "match", ("match_type",), _string_value, default="unknown"
    )


def _extract_is_recruiter(row: dict[str, Any]) -> bool:
    return _extract_nested_value(row, "match", ("is_recruiter",), bool, default=False)


def _extract_route(row: dict[str, Any]) -> str:
    sponsor = _coerce_sponsor(row)
    return _string_value(sponsor.get("route"))


def _extract_title(row: dict[str, Any]) -> str:
    return _string_value(_coerce_offer(row).get("title"))


def _job_key(row: dict[str, Any]) -> tuple[str, str, str]:
    offer = _coerce_offer(row)
    return (
        _string_value(offer.get("title"), default="").casefold(),
        _string_value(offer.get("company"), default="").casefold(),
        _string_value(offer.get("location"), default="").casefold(),
    )


def _ranking_key(row: dict[str, Any]) -> tuple[float, int, int]:
    score = _extract_score(row)
    recruiter_rank = 0 if _extract_is_recruiter(row) else 1
    match_type_rank = -MATCH_TYPE_PRIORITY.get(
        _extract_match_type(row),
        len(MATCH_TYPE_PRIORITY),
    )
    return score, recruiter_rank, match_type_rank


def _deduplicate_matches(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    best_rows: dict[tuple[str, str, str], dict[str, Any]] = {}
    for row in rows:
        key = _job_key(row)
        current = best_rows.get(key)
        if current is None or _ranking_key(row) > _ranking_key(current):
            best_rows[key] = row
    return list(best_rows.values())


def _build_weighted_breakdown(
    rows: list[dict[str, Any]],
    key_func: Callable[[dict[str, Any]], str],
    field_name: str,
) -> list[dict[str, Any]]:
    weighted_values: dict[str, float] = {}
    raw_counts: Counter[str] = Counter()

    for row in rows:
        label = key_func(row)
        raw_counts[label] += 1
        weighted_values[label] = weighted_values.get(label, 0.0) + _extract_weight(row)

    return _weighted_rows(weighted_values, raw_counts, field_name)


def _score_counts(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    weighted_values = {label: 0.0 for _, _, label in SCORE_LABELS}
    raw_counts: Counter[str] = Counter({label: 0 for _, _, label in SCORE_LABELS})

    for row in rows:
        score = _extract_score(row)
        match_type = _extract_match_type(row)
        label = next(
            (
                mapped_label
                for mapped_score, mapped_type, mapped_label in SCORE_LABELS
                if round(score, 2) == mapped_score and match_type == mapped_type
            ),
            f"{score:.2f} {match_type}",
        )
        raw_counts[label] += 1
        weighted_values[label] = weighted_values.get(label, 0.0) + _extract_weight(row)

    return _weighted_rows(weighted_values, raw_counts, "label")


def _build_dataset(
    rows: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    all_matches = _deduplicate_matches(rows)
    high_confidence_matches = [
        row for row in all_matches if _extract_score(row) >= HIGH_CONFIDENCE_SCORE
    ]
    return all_matches, high_confidence_matches


def _normalize_title_tokens(title: str) -> list[str]:
    cleaned = re.sub(r"[^a-z0-9]+", " ", title.casefold())
    return [
        token for token in cleaned.split() if token and token not in TITLE_STOPWORDS
    ]


def _strip_seniority_tokens(tokens: list[str]) -> list[str]:
    seniority_tokens = {
        "apprentice",
        "associate",
        "chief",
        "cto",
        "director",
        "entry",
        "graduate",
        "head",
        "intern",
        "junior",
        "lead",
        "manager",
        "principal",
        "senior",
        "specialist",
        "sr",
        "staff",
        "trainee",
        "vp",
    }
    stripped = [token for token in tokens if token not in seniority_tokens]
    return stripped or tokens


def _title_similarity(left_tokens: list[str], right_tokens: list[str]) -> float:
    left = " ".join(left_tokens)
    right = " ".join(right_tokens)
    if not left or not right:
        return 0.0

    left_set = set(left_tokens)
    right_set = set(right_tokens)
    overlap = len(left_set & right_set) / max(1, min(len(left_set), len(right_set)))
    ratio = SequenceMatcher(None, left, right).ratio()
    return max(overlap, ratio)


def _weighted_rows(
    weighted_values: dict[str, float],
    raw_counts: Counter[str],
    field_name: str,
) -> list[dict[str, Any]]:
    return [
        {
            field_name: label,
            "weighted_count": round(weighted_values[label], 4),
            "raw_count": raw_counts[label],
        }
        for label in sorted(
            weighted_values,
            key=lambda label: (-weighted_values[label], -raw_counts[label], label),
        )
    ]


def _choose_cluster_label(
    weighted_variants: dict[str, float],
    raw_variants: Counter[str],
) -> str:
    return sorted(
        weighted_variants,
        key=lambda label: (
            -weighted_variants[label],
            -raw_variants[label],
            len(label),
            label,
        ),
    )[0]


def _cluster_titles(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    clusters: list[dict[str, Any]] = []

    for row in rows:
        raw_title = _extract_title(row)
        tokens = _normalize_title_tokens(raw_title)
        family_tokens = _strip_seniority_tokens(tokens)
        if not family_tokens:
            family_tokens = tokens

        best_cluster: dict[str, Any] | None = None
        best_score = 0.0
        for cluster in clusters:
            similarity = _title_similarity(
                family_tokens,
                cluster["family_tokens"],
            )
            if similarity >= TITLE_GROUP_THRESHOLD and similarity > best_score:
                best_cluster = cluster
                best_score = similarity

        weight = _extract_weight(row)

        if best_cluster is None:
            clusters.append(
                {
                    "family_tokens": family_tokens,
                    "weighted_count": weight,
                    "raw_count": 1,
                    "weighted_variants": {raw_title: weight},
                    "raw_variants": Counter([raw_title]),
                }
            )
            continue

        best_cluster["weighted_count"] += weight
        best_cluster["raw_count"] += 1
        best_cluster["weighted_variants"][raw_title] = (
            best_cluster["weighted_variants"].get(raw_title, 0.0) + weight
        )
        best_cluster["raw_variants"][raw_title] += 1

    title_rows = []
    for cluster in clusters:
        title_rows.append(
            {
                "title": _choose_cluster_label(
                    cluster["weighted_variants"],
                    cluster["raw_variants"],
                ),
                "weighted_count": round(cluster["weighted_count"], 4),
                "raw_count": cluster["raw_count"],
            }
        )

    return sorted(
        title_rows,
        key=lambda item: (-item["weighted_count"], -item["raw_count"], item["title"]),
    )


def _classify_seniority(title: str) -> str:
    lowered = title.casefold()
    for label, markers in SENIORITY_PATTERNS:
        if any(re.search(rf"\b{re.escape(marker)}\b", lowered) for marker in markers):
            return label
    return "Standard"


def _format_rate(value: float) -> str:
    return f"{value * 100:.2f}%"


def _format_keywords(keywords: str) -> str:
    cleaned = keywords.strip()
    return cleaned if cleaned else "No keyword filter"


def _format_weight(value: Any) -> str:
    return f"{_safe_float(value):.2f}"


def _top_rows(
    rows: list[dict[str, Any]], field_name: str, label: str, limit: int = 10
) -> list[str]:
    if not rows:
        return [
            f"| No {label.lower()} available | Weighted score | Raw jobs |",
            "|---|---|---|",
            "| None | 0.00 | 0 |",
        ]

    lines = [f"| {label} | Weighted score | Raw jobs |", "|---|---|---|"]
    for item in rows[:limit]:
        lines.append(
            f"| {_string_value(item.get(field_name))} | {_format_weight(item.get('weighted_count'))} | {_safe_int(item.get('raw_count'))} |"
        )
    return lines


def render_market_analytics_markdown(
    analytics: dict[str, Any],
    matches: Any,
    *,
    generated_at: str,
    keywords: str = "",
) -> str:
    metadata, rows = _coerce_metadata_and_rows(matches)
    overview = analytics.get("overview", {})
    searched_locations = metadata.get("locations", [])
    if not isinstance(searched_locations, list):
        searched_locations = []

    lines: list[str] = [
        "# Market Analytics",
        "",
        f"Last research run (UTC): {generated_at}",
        f"Generated at: {generated_at}",
        "",
        "## Scope",
        "",
        f"- Filtering keywords: {_format_keywords(keywords)}",
        "- Analytics are computed on unique jobs deduplicated by title + company + location.",
        "- Every analytics entry, chart, and category table is weighted by the match quality score.",
        "- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.",
        f"- Raw matched rows before deduplication: {len(rows)}",
        f"- Unique matched jobs: {_safe_int(overview.get('matched_jobs'))}",
    ]

    if searched_locations:
        lines.append(
            f"- Search locations: {', '.join(_string_value(item, default='') for item in searched_locations if _string_value(item, default=''))}"
        )

    lines.extend(
        [
            "",
            "## Overview",
            "",
            f"- Total jobs fetched: {_safe_int(overview.get('total_jobs'))}",
            f"- Unique matched jobs: {_safe_int(overview.get('matched_jobs'))}",
            f"- High-confidence unique jobs: {_safe_int(overview.get('high_confidence_jobs'))}",
            f"- Weighted matched jobs: {_format_weight(overview.get('weighted_matched_jobs'))}",
            f"- Weighted high-confidence jobs: {_format_weight(overview.get('weighted_high_confidence_jobs'))}",
            f"- Weighted match rate: {_format_rate(_safe_float(overview.get('match_rate')))}",
            f"- Weighted high-confidence rate: {_format_rate(_safe_float(overview.get('high_confidence_rate')))}",
            "",
            "## Charts",
            "",
            "All charts below use quality-score-weighted totals rather than raw row counts.",
            "",
            "### Top Locations",
            "",
            "![Top locations chart](../charts/top_locations.png)",
            "",
            "### Top Employers (High Confidence)",
            "",
            "![Top employers chart](../charts/top_employers.png)",
            "",
            "### Match Quality Distribution",
            "",
            "![Match quality chart](../charts/match_quality.png)",
            "",
            "### Top Job Title Families",
            "",
            "![Top title families chart](../charts/top_titles.png)",
            "",
            "### Visa Routes",
            "",
            "![Visa routes chart](../charts/routes.png)",
            "",
            "### Title Seniority",
            "",
            "![Title seniority chart](../charts/seniority.png)",
            "",
            "## Top Locations",
            "",
        ]
    )
    lines.extend(_top_rows(analytics.get("locations", []), "location", "Location"))
    lines.extend(["", "## Top Employers (High Confidence)", ""])
    lines.extend(_top_rows(analytics.get("employers", []), "company", "Company"))
    lines.extend(["", "## Top Job Title Families", ""])
    lines.extend(_top_rows(analytics.get("titles", []), "title", "Title Family"))
    lines.extend(["", "## Visa Routes", ""])
    lines.extend(_top_rows(analytics.get("routes", []), "route", "Route"))
    lines.extend(["", "## Title Seniority", ""])
    lines.extend(_top_rows(analytics.get("seniority", []), "level", "Seniority"))
    lines.extend(
        [
            "",
            "## Match Quality Breakdown",
            "",
            "| Label | Weighted score | Raw jobs |",
            "|---|---|---|",
        ]
    )

    score_rows = analytics.get("scores", [])
    if score_rows:
        for item in score_rows:
            lines.append(
                f"| {_string_value(item.get('label'))} | {_format_weight(item.get('weighted_count'))} | {_safe_int(item.get('raw_count'))} |"
            )
    else:
        lines.append("| None | 0.00 | 0 |")

    lines.append("")
    return "\n".join(lines)


def render_market_analytics_hugo_content(markdown: str, generated_at: str) -> str:
    return _ANALYTICS_FRONTMATTER.format(generated_at=generated_at) + markdown


def build_market_analytics(matches: Any) -> dict[str, Any]:
    metadata, rows = _coerce_metadata_and_rows(matches)
    all_matches, high_confidence_matches = _build_dataset(rows)

    total_jobs = _safe_int(metadata.get("job_offers_fetched"), default=len(all_matches))
    if total_jobs < len(all_matches):
        total_jobs = len(all_matches)

    matched_jobs = len(all_matches)
    high_confidence_jobs = len(high_confidence_matches)
    weighted_matched_jobs = round(
        sum(_extract_weight(row) for row in all_matches),
        4,
    )
    weighted_high_confidence_jobs = round(
        sum(_extract_weight(row) for row in high_confidence_matches),
        4,
    )

    return {
        "overview": {
            "total_jobs": total_jobs,
            "matched_jobs": matched_jobs,
            "high_confidence_jobs": high_confidence_jobs,
            "weighted_matched_jobs": weighted_matched_jobs,
            "weighted_high_confidence_jobs": weighted_high_confidence_jobs,
            "match_rate": (
                round(weighted_matched_jobs / total_jobs, 4) if total_jobs else 0.0
            ),
            "high_confidence_rate": (
                round(
                    weighted_high_confidence_jobs / total_jobs,
                    4,
                )
                if total_jobs
                else 0.0
            ),
        },
        "locations": _build_weighted_breakdown(
            all_matches,
            lambda row: _string_value(_coerce_offer(row).get("location")),
            "location",
        ),
        "employers": _build_weighted_breakdown(
            high_confidence_matches,
            lambda row: _string_value(_coerce_offer(row).get("company")),
            "company",
        ),
        "titles": _cluster_titles(all_matches),
        "routes": _build_weighted_breakdown(all_matches, _extract_route, "route"),
        "seniority": _build_weighted_breakdown(
            all_matches,
            lambda row: _classify_seniority(_extract_title(row)),
            "level",
        ),
        "scores": _score_counts(all_matches),
    }


def _plot_bar_chart(
    labels: list[str],
    counts: list[float],
    *,
    title: str,
    ylabel: str,
    output_path: Path,
) -> None:
    try:
        plt = import_module("matplotlib.pyplot")
    except ImportError as exc:
        raise RuntimeError(
            "matplotlib is required to generate analytics charts."
        ) from exc

    ensure_parent_dir(output_path)
    figure, axis = plt.subplots(figsize=(12, 7))

    if labels and counts:
        axis.bar(labels, counts)
        axis.set_ylabel(ylabel)
        axis.tick_params(axis="x", rotation=35)
    else:
        axis.text(0.5, 0.5, "No data available", ha="center", va="center")
        axis.set_xticks([])
        axis.set_yticks([])

    axis.set_title(title)
    figure.tight_layout()
    figure.savefig(str(output_path), format="png", dpi=150, bbox_inches="tight")
    plt.close(figure)


def _generate_category_chart(
    analytics: dict[str, Any],
    category: str,
    label_field: str,
    chart_title: str,
    output_path: Path,
    limit: int = 10,
) -> None:
    """Generate a bar chart for a category from analytics data."""
    items = analytics.get(category, [])[:limit]
    labels = [_string_value(item.get(label_field)) for item in items]
    counts = [_safe_float(item.get("weighted_count")) for item in items]
    _plot_bar_chart(
        labels=labels,
        counts=counts,
        title=chart_title,
        ylabel="Weighted jobs",
        output_path=output_path,
    )


def generate_charts(
    analytics: dict[str, Any],
    matches: Any,
    output_dir: Path | str,
) -> None:
    charts_dir = Path(output_dir)
    charts_dir.mkdir(parents=True, exist_ok=True)

    # Chart configuration: (category, label_field, title, output_file, limit)
    chart_configs = [
        ("locations", "location", "Top Locations", "top_locations.png", 10),
        (
            "employers",
            "company",
            "Top High-Confidence Employers",
            "top_employers.png",
            10,
        ),
        ("titles", "title", "Top Job Title Families", "top_titles.png", 10),
        ("routes", "route", "Visa Route Distribution", "routes.png", None),
        ("seniority", "level", "Title Seniority Distribution", "seniority.png", None),
    ]

    for category, label_field, title, filename, limit in chart_configs:
        _generate_category_chart(
            analytics,
            category,
            label_field,
            title,
            charts_dir / filename,
            limit=limit or 10,
        )

    # Special handling for score chart (uses 'label' field instead)
    score_counts = analytics.get("scores", [])
    _plot_bar_chart(
        labels=[_string_value(item.get("label"), default="") for item in score_counts],
        counts=[_safe_float(item.get("weighted_count")) for item in score_counts],
        title="Match Quality Distribution",
        ylabel="Weighted jobs",
        output_path=charts_dir / "match_quality.png",
    )


def save_market_analytics_outputs(
    matches: Any,
    *,
    json_output_path: Path | str = DEFAULT_MARKET_ANALYTICS_OUTPUT,
    markdown_output_path: Path | str = DEFAULT_MARKET_ANALYTICS_MARKDOWN_OUTPUT,
    site_markdown_output_path: Path | str = DEFAULT_SITE_ANALYTICS_OUTPUT,
    charts_output_dir: Path | str = DEFAULT_CHARTS_OUTPUT_DIR,
    keywords: str = "",
) -> dict[str, Any]:
    generated_at = datetime.now(timezone.utc).isoformat()
    analytics = build_market_analytics(matches)
    write_json(Path(json_output_path), analytics)
    generate_charts(analytics, matches, charts_output_dir)
    markdown = render_market_analytics_markdown(
        analytics,
        matches,
        generated_at=generated_at,
        keywords=keywords,
    )
    write_text(Path(markdown_output_path), markdown)
    write_text(
        Path(site_markdown_output_path),
        render_market_analytics_hugo_content(markdown, generated_at),
    )
    return analytics


__all__ = [
    "DEFAULT_CHARTS_OUTPUT_DIR",
    "DEFAULT_MARKET_ANALYTICS_OUTPUT",
    "DEFAULT_MARKET_ANALYTICS_MARKDOWN_OUTPUT",
    "DEFAULT_SITE_ANALYTICS_OUTPUT",
    "build_market_analytics",
    "generate_charts",
    "render_market_analytics_hugo_content",
    "render_market_analytics_markdown",
    "save_market_analytics_outputs",
]
