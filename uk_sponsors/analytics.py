from __future__ import annotations

from collections import Counter
from importlib import import_module
from pathlib import Path
from typing import Any, Iterable

from .json_io import ensure_parent_dir, write_json

OUTPUT_ROOT = Path("output")
DEFAULT_MARKET_ANALYTICS_OUTPUT = OUTPUT_ROOT / "reports" / "market_analytics.json"
DEFAULT_CHARTS_OUTPUT_DIR = OUTPUT_ROOT / "site" / "static" / "charts"

HIGH_CONFIDENCE_SCORE = 0.92

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


def _coerce_offer(row: dict[str, Any]) -> dict[str, Any]:
    offer = row.get("offer", {})
    if isinstance(offer, dict):
        return offer
    return {}


def _coerce_match(row: dict[str, Any]) -> dict[str, Any]:
    match = row.get("match", {})
    if isinstance(match, dict):
        return match
    return {}


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


def _extract_match_type(row: dict[str, Any]) -> str:
    nested_match = _coerce_match(row)
    match_type = nested_match.get("match_type") or row.get("match_type")
    return _string_value(match_type, default="unknown")


def _extract_is_recruiter(row: dict[str, Any]) -> bool:
    nested_match = _coerce_match(row)
    value = nested_match.get("is_recruiter")
    if value is None:
        value = row.get("is_recruiter")
    return bool(value)


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


def _sorted_counter_rows(
    counter: Counter[str], field_name: str
) -> list[dict[str, Any]]:
    return [
        {field_name: label, "count": count}
        for label, count in sorted(
            counter.items(), key=lambda item: (-item[1], item[0])
        )
    ]


def _score_counts(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    counts = Counter()
    known_labels: set[str] = set()

    for score, match_type, label in SCORE_LABELS:
        counts[label] = 0
        known_labels.add(label)

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
        counts[label] += 1
        known_labels.add(label)

    ordered_labels = [label for _, _, label in SCORE_LABELS]
    extra_labels = sorted(
        label for label in known_labels if label not in ordered_labels
    )
    return [
        {"label": label, "count": counts[label]}
        for label in ordered_labels + extra_labels
    ]


def _build_dataset(
    rows: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    all_matches = _deduplicate_matches(rows)
    high_confidence_matches = [
        row for row in all_matches if _extract_score(row) >= HIGH_CONFIDENCE_SCORE
    ]
    return all_matches, high_confidence_matches


def build_market_analytics(matches: Any) -> dict[str, Any]:
    metadata, rows = _coerce_metadata_and_rows(matches)
    all_matches, high_confidence_matches = _build_dataset(rows)

    total_jobs = _safe_int(metadata.get("job_offers_fetched"), default=len(all_matches))
    if total_jobs < len(all_matches):
        total_jobs = len(all_matches)

    matched_jobs = len(all_matches)
    high_confidence_jobs = len(high_confidence_matches)

    locations = Counter(
        _string_value(_coerce_offer(row).get("location")) for row in all_matches
    )
    employers = Counter(
        _string_value(_coerce_offer(row).get("company"))
        for row in high_confidence_matches
    )

    return {
        "overview": {
            "total_jobs": total_jobs,
            "matched_jobs": matched_jobs,
            "high_confidence_jobs": high_confidence_jobs,
            "match_rate": round(matched_jobs / total_jobs, 4) if total_jobs else 0.0,
            "high_confidence_rate": (
                round(high_confidence_jobs / total_jobs, 4) if total_jobs else 0.0
            ),
        },
        "locations": _sorted_counter_rows(locations, "location"),
        "employers": _sorted_counter_rows(employers, "company"),
        "scores": _score_counts(all_matches),
    }


def _plot_bar_chart(
    labels: list[str],
    counts: list[int],
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


def generate_charts(
    analytics: dict[str, Any],
    matches: Any,
    output_dir: Path | str,
) -> None:
    _, rows = _coerce_metadata_and_rows(matches)
    all_matches, high_confidence_matches = _build_dataset(rows)
    charts_dir = Path(output_dir)
    charts_dir.mkdir(parents=True, exist_ok=True)

    top_locations = analytics.get("locations", [])[:10]
    _plot_bar_chart(
        labels=[_string_value(item.get("location")) for item in top_locations],
        counts=[_safe_int(item.get("count")) for item in top_locations],
        title="Top Locations",
        ylabel="Jobs",
        output_path=charts_dir / "top_locations.png",
    )

    employer_counts = Counter(
        _string_value(_coerce_offer(row).get("company"))
        for row in high_confidence_matches
    )
    top_employers = sorted(
        employer_counts.items(),
        key=lambda item: (-item[1], item[0]),
    )[:10]
    _plot_bar_chart(
        labels=[label for label, _ in top_employers],
        counts=[count for _, count in top_employers],
        title="Top High-Confidence Employers",
        ylabel="Jobs",
        output_path=charts_dir / "top_employers.png",
    )

    score_counts = analytics.get("scores", _score_counts(all_matches))
    _plot_bar_chart(
        labels=[_string_value(item.get("label"), default="") for item in score_counts],
        counts=[_safe_int(item.get("count")) for item in score_counts],
        title="Match Quality Distribution",
        ylabel="Jobs",
        output_path=charts_dir / "match_quality.png",
    )


def save_market_analytics_outputs(
    matches: Any,
    *,
    json_output_path: Path | str = DEFAULT_MARKET_ANALYTICS_OUTPUT,
    charts_output_dir: Path | str = DEFAULT_CHARTS_OUTPUT_DIR,
) -> dict[str, Any]:
    analytics = build_market_analytics(matches)
    write_json(Path(json_output_path), analytics)
    generate_charts(analytics, matches, charts_output_dir)
    return analytics


__all__ = [
    "DEFAULT_CHARTS_OUTPUT_DIR",
    "DEFAULT_MARKET_ANALYTICS_OUTPUT",
    "build_market_analytics",
    "generate_charts",
    "save_market_analytics_outputs",
]
