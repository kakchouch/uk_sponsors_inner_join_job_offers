from __future__ import annotations

from difflib import SequenceMatcher
import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path
from typing import Any, cast

from .job_offers import DEFAULT_CONFIG_PATH, JobOffersRequest, build_job_offers_payload
from .json_io import read_json
from .registered_sponsors import SponsorsRequest, build_sponsors_payload

_HUGO_FRONTMATTER = """\
+++
title = "Latest Sponsored Jobs"
description = "Most recent matched records produced by the project pipeline for the curated city list."
lastmod = "{generated_at}"
last_research_at = "{generated_at}"
+++

"""

LEGAL_SUFFIXES = {
    "co",
    "company",
    "corp",
    "corporation",
    "inc",
    "limited",
    "llc",
    "llp",
    "ltd",
    "plc",
    "uk",
}

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = PROJECT_ROOT / "input"
ALIAS_TABLE_PATH = INPUT_DIR / "alias_table.json"
HEADHUNTERS_PATH = INPUT_DIR / "headhunters.json"

EXACT_NORMALIZED_MATCH_SCORE = 1.00
ALIAS_MATCH_SCORE = 0.92
FUZZY_STRONG_MATCH_SCORE = 0.85
RECRUITER_OR_AMBIGUOUS_MATCH_SCORE = 0.50
SUBSTRING_ONLY_MATCH_SCORE = 0.20

EXACT_NORMALIZED_MATCH = "exact_normalized"
ALIAS_TABLE_MATCH = "alias_table"
FUZZY_STRONG_MATCH = "fuzzy_strong"
RECRUITER_OR_AMBIGUOUS_MATCH = "recruiter_or_ambiguous"
SUBSTRING_ONLY_MATCH = "substring_only"

MATCH_TYPE_PRIORITY = {
    EXACT_NORMALIZED_MATCH: 0,
    ALIAS_TABLE_MATCH: 1,
    FUZZY_STRONG_MATCH: 2,
    RECRUITER_OR_AMBIGUOUS_MATCH: 3,
    SUBSTRING_ONLY_MATCH: 4,
}


@dataclass(frozen=True)
class MatchRecord:
    offer: dict[str, Any]
    sponsor: dict[str, str]
    score: float
    match_type: str


@dataclass(frozen=True)
class CandidateMatch:
    sponsor: dict[str, str]
    sponsor_normalized: str
    ranking_key: tuple[float, float, int]


@dataclass(frozen=True)
class MatchingResources:
    alias_to_canonical: dict[str, str]
    recruiter_names: set[str]


@dataclass(frozen=True)
class ReportRequest:
    keywords: str = ""
    location: str = ""
    locations: tuple[str, ...] = ()
    locations_file: str = ""
    page: int = 1
    results_per_page: int = 20
    sources: tuple[str, ...] = ()
    config_path: Path = DEFAULT_CONFIG_PATH
    job_timeout: int = 20
    sponsor_timeout: int = 30
    single_page: bool = False
    max_pages: int = 0


@dataclass(frozen=True)
class ReportArtifacts:
    generated_at: str
    jobs_payload: dict[str, Any]
    sponsors_payload: dict[str, Any]
    matches: list[MatchRecord]
    markdown: str
    hugo_markdown: str
    matched_payload: dict[str, Any]


def normalize_company_name(value: str) -> str:
    lowered = value.lower().replace("&", " and ")
    cleaned = re.sub(r"[^a-z0-9]+", " ", lowered)
    tokens = [item for item in cleaned.split() if item and item not in LEGAL_SUFFIXES]
    return " ".join(tokens)


def _load_alias_to_canonical(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}

    payload = read_json(path)
    aliases: dict[str, str] = {}
    for entry in payload.get("aliases", []):
        canonical = normalize_company_name(str(entry.get("canonical") or ""))
        if not canonical:
            continue

        aliases[canonical] = canonical
        for alias in entry.get("aliases", []):
            normalized_alias = normalize_company_name(str(alias or ""))
            if normalized_alias:
                aliases[normalized_alias] = canonical

    return aliases


def _load_recruiter_names(path: Path) -> set[str]:
    if not path.exists():
        return set()

    payload = read_json(path)
    recruiters: set[str] = set()
    for agency in payload.get("agencies", []):
        name = normalize_company_name(str(agency.get("name") or ""))
        if name:
            recruiters.add(name)

        for alias in agency.get("aliases", []):
            normalized_alias = normalize_company_name(str(alias or ""))
            if normalized_alias:
                recruiters.add(normalized_alias)

    return recruiters


@lru_cache(maxsize=1)
def load_matching_resources() -> MatchingResources:
    return MatchingResources(
        alias_to_canonical=_load_alias_to_canonical(ALIAS_TABLE_PATH),
        recruiter_names=_load_recruiter_names(HEADHUNTERS_PATH),
    )


def build_sponsor_indexes(
    sponsors: list[dict[str, str]],
) -> tuple[
    dict[str, list[dict[str, str]]],
    dict[str, set[int]],
    dict[str, set[int]],
    list[str],
]:
    by_name: dict[str, list[dict[str, str]]] = defaultdict(list)
    token_to_indices: dict[str, set[int]] = defaultdict(set)
    token_prefix_to_indices: dict[str, set[int]] = defaultdict(set)
    normalized_names: list[str] = []

    for index, sponsor in enumerate(sponsors):
        normalized = normalize_company_name(sponsor.get("organisation_name", ""))
        normalized_names.append(normalized)
        if normalized:
            by_name[normalized].append(sponsor)

        for token in set(normalized.split()):
            if len(token) >= 3:
                token_to_indices[token].add(index)
            if len(token) >= 4:
                token_prefix_to_indices[token[:4]].add(index)

    return by_name, token_to_indices, token_prefix_to_indices, normalized_names


def is_substring_match(company_normalized: str, sponsor_normalized: str) -> bool:
    if not company_normalized or not sponsor_normalized:
        return False

    if company_normalized in sponsor_normalized and len(company_normalized) >= 6:
        return True

    if sponsor_normalized in company_normalized and len(sponsor_normalized) >= 6:
        return True

    return False


def build_candidate_indices(
    company_normalized: str,
    token_to_indices: dict[str, set[int]],
    token_prefix_to_indices: dict[str, set[int]],
) -> set[int]:
    candidate_indices: set[int] = set()
    tokens = set(company_normalized.split())
    for token in tokens:
        candidate_indices.update(token_to_indices.get(token, set()))

    if candidate_indices:
        return candidate_indices

    for token in tokens:
        if len(token) >= 4:
            candidate_indices.update(token_prefix_to_indices.get(token[:4], set()))

    return candidate_indices


def is_alias_match(
    company_normalized: str,
    sponsor_normalized: str,
    alias_to_canonical: dict[str, str],
) -> bool:
    company_canonical = alias_to_canonical.get(company_normalized)
    if not company_canonical:
        return False

    return company_canonical == alias_to_canonical.get(
        sponsor_normalized, sponsor_normalized
    )


def calculate_similarity_metrics(
    company_normalized: str,
    sponsor_normalized: str,
) -> tuple[float, float, int]:
    company_tokens = set(company_normalized.split())
    sponsor_tokens = set(sponsor_normalized.split())
    shared_token_count = len(company_tokens & sponsor_tokens)
    overlap_ratio = shared_token_count / max(
        1, min(len(company_tokens), len(sponsor_tokens))
    )
    ratio = SequenceMatcher(None, company_normalized, sponsor_normalized).ratio()
    length_gap = abs(len(company_normalized) - len(sponsor_normalized))
    return ratio, overlap_ratio, length_gap


def is_fuzzy_strong_match(company_normalized: str, sponsor_normalized: str) -> bool:
    if not company_normalized or not sponsor_normalized:
        return False

    if is_substring_match(company_normalized, sponsor_normalized):
        return False

    ratio, overlap_ratio, length_gap = calculate_similarity_metrics(
        company_normalized,
        sponsor_normalized,
    )
    if ratio >= 0.92:
        return True

    if ratio >= 0.86 and overlap_ratio >= 0.75 and length_gap <= 12:
        return True

    return False


def select_best_candidates(candidates: list[CandidateMatch]) -> list[CandidateMatch]:
    if not candidates:
        return []

    best_key = max(candidate.ranking_key for candidate in candidates)
    return [candidate for candidate in candidates if candidate.ranking_key == best_key]


def build_match_records(
    offer: dict[str, Any],
    candidates: list[CandidateMatch],
    score: float,
    match_type: str,
) -> list[MatchRecord]:
    return [
        MatchRecord(
            offer=offer,
            sponsor=candidate.sponsor,
            score=score,
            match_type=match_type,
        )
        for candidate in candidates
    ]


def freeze_value(value: Any) -> Any:
    if isinstance(value, dict):
        return tuple(
            sorted((str(key), freeze_value(item)) for key, item in value.items())
        )

    if isinstance(value, list):
        return tuple(freeze_value(item) for item in value)

    if isinstance(value, tuple):
        return tuple(freeze_value(item) for item in value)

    if isinstance(value, set):
        return tuple(sorted(freeze_value(item) for item in value))

    return value


def build_match_dedup_key(match: MatchRecord) -> tuple[Any, ...]:
    return (
        freeze_value(match.offer),
        freeze_value(match.sponsor),
        match.score,
        match.match_type,
    )


def deduplicate_matches(matches: list[MatchRecord]) -> list[MatchRecord]:
    deduplicated: list[MatchRecord] = []
    seen_keys: set[tuple[Any, ...]] = set()

    for match in matches:
        dedup_key = build_match_dedup_key(match)
        if dedup_key in seen_keys:
            continue

        seen_keys.add(dedup_key)
        deduplicated.append(match)

    return deduplicated


def build_match_sort_key(
    match: MatchRecord,
) -> tuple[float, int, str, str, str, str, str]:
    offer = match.offer
    sponsor = match.sponsor
    return (
        -match.score,
        MATCH_TYPE_PRIORITY.get(match.match_type, len(MATCH_TYPE_PRIORITY)),
        str(offer.get("company") or "").lower(),
        str(offer.get("title") or "").lower(),
        str(offer.get("location") or "").lower(),
        str(sponsor.get("organisation_name") or "").lower(),
        str(offer.get("url") or "").lower(),
    )


def match_offers_with_sponsors(
    offers: list[dict[str, Any]],
    sponsors: list[dict[str, str]],
) -> list[MatchRecord]:
    resources = load_matching_resources()
    by_name, token_to_indices, token_prefix_to_indices, normalized_sponsor_names = (
        build_sponsor_indexes(sponsors)
    )
    matches: list[MatchRecord] = []

    for offer in offers:
        company_name = str(offer.get("company") or "")
        company_normalized = normalize_company_name(company_name)
        if not company_normalized:
            continue

        exact_matches = by_name.get(company_normalized, [])
        if exact_matches:
            for sponsor in exact_matches:
                matches.append(
                    MatchRecord(
                        offer=offer,
                        sponsor=sponsor,
                        score=EXACT_NORMALIZED_MATCH_SCORE,
                        match_type=EXACT_NORMALIZED_MATCH,
                    )
                )
            continue

        canonical_company = resources.alias_to_canonical.get(company_normalized)
        if canonical_company:
            alias_matches = by_name.get(canonical_company, [])
            if alias_matches:
                for sponsor in alias_matches:
                    matches.append(
                        MatchRecord(
                            offer=offer,
                            sponsor=sponsor,
                            score=ALIAS_MATCH_SCORE,
                            match_type=ALIAS_TABLE_MATCH,
                        )
                    )
                continue

        candidate_indices = build_candidate_indices(
            company_normalized,
            token_to_indices,
            token_prefix_to_indices,
        )
        fuzzy_candidates: list[CandidateMatch] = []
        recruiter_candidates: list[CandidateMatch] = []
        substring_candidates: list[CandidateMatch] = []

        for index in candidate_indices:
            sponsor_normalized = normalized_sponsor_names[index]
            sponsor = sponsors[index]
            ratio, overlap_ratio, length_gap = calculate_similarity_metrics(
                company_normalized,
                sponsor_normalized,
            )

            if is_alias_match(
                company_normalized,
                sponsor_normalized,
                resources.alias_to_canonical,
            ):
                matches.append(
                    MatchRecord(
                        offer=offer,
                        sponsor=sponsor,
                        score=ALIAS_MATCH_SCORE,
                        match_type=ALIAS_TABLE_MATCH,
                    )
                )
                continue

            recruiter_candidates.append(
                CandidateMatch(
                    sponsor=sponsor,
                    sponsor_normalized=sponsor_normalized,
                    ranking_key=(ratio, overlap_ratio, -length_gap),
                )
            )

            if is_fuzzy_strong_match(company_normalized, sponsor_normalized):
                fuzzy_candidates.append(
                    CandidateMatch(
                        sponsor=sponsor,
                        sponsor_normalized=sponsor_normalized,
                        ranking_key=(ratio, overlap_ratio, -length_gap),
                    )
                )
                continue

            if is_substring_match(company_normalized, sponsor_normalized):
                substring_candidates.append(
                    CandidateMatch(
                        sponsor=sponsor,
                        sponsor_normalized=sponsor_normalized,
                        ranking_key=(overlap_ratio, ratio, -length_gap),
                    )
                )

        company_is_recruiter = company_normalized in resources.recruiter_names

        if company_is_recruiter and recruiter_candidates:
            selected_candidates = select_best_candidates(recruiter_candidates)
            matches.extend(
                build_match_records(
                    offer,
                    selected_candidates,
                    RECRUITER_OR_AMBIGUOUS_MATCH_SCORE,
                    RECRUITER_OR_AMBIGUOUS_MATCH,
                )
            )
            continue

        if fuzzy_candidates:
            selected_candidates = select_best_candidates(fuzzy_candidates)
            if len(selected_candidates) > 1:
                matches.extend(
                    build_match_records(
                        offer,
                        selected_candidates,
                        RECRUITER_OR_AMBIGUOUS_MATCH_SCORE,
                        RECRUITER_OR_AMBIGUOUS_MATCH,
                    )
                )
                continue

            matches.extend(
                build_match_records(
                    offer,
                    selected_candidates,
                    FUZZY_STRONG_MATCH_SCORE,
                    FUZZY_STRONG_MATCH,
                )
            )
            continue

        if substring_candidates:
            selected_candidates = select_best_candidates(substring_candidates)
            if len(selected_candidates) > 1:
                matches.extend(
                    build_match_records(
                        offer,
                        selected_candidates,
                        RECRUITER_OR_AMBIGUOUS_MATCH_SCORE,
                        RECRUITER_OR_AMBIGUOUS_MATCH,
                    )
                )
                continue

            matches.extend(
                build_match_records(
                    offer,
                    selected_candidates,
                    SUBSTRING_ONLY_MATCH_SCORE,
                    SUBSTRING_ONLY_MATCH,
                )
            )

    matches = deduplicate_matches(matches)
    matches.sort(key=build_match_sort_key)

    return matches


def escape_markdown_cell(value: Any) -> str:
    text = str(value) if value is not None else ""
    return text.replace("|", "\\|").replace("\n", " ").strip()


def render_hugo_content(markdown: str, generated_at: str) -> str:
    return _HUGO_FRONTMATTER.format(generated_at=generated_at) + markdown


def render_markdown(
    matches: list[MatchRecord],
    jobs_payload: dict[str, Any],
    sponsors_payload: dict[str, Any],
    generated_at: str,
) -> str:
    jobs_meta = jobs_payload.get("metadata", {})
    sponsors_meta = sponsors_payload.get("metadata", {})
    searched_locations = jobs_meta.get("locations", [])

    lines: list[str] = [
        "# Sponsored Job Matches",
        "",
        f"Last research run (UTC): {generated_at}",
        f"Generated at: {generated_at}",
        "",
        "## Summary",
        "",
        f"- Job offers fetched: {jobs_meta.get('total_offers', 0)}",
        f"- Sponsors fetched: {sponsors_meta.get('total_sponsors', 0)}",
        f"- Matched rows: {len(matches)}",
    ]

    if searched_locations:
        lines.append(f"- Search locations: {', '.join(searched_locations)}")

    lines.extend(
        [
            "",
            "## Matches",
            "",
            "| Score | Match Type | Company | Job Title | Location | Source | Sponsor | Sponsor Town/City | Route | Job URL |",
            "|---|---|---|---|---|---|---|---|---|---|",
        ]
    )

    for item in matches:
        offer = item.offer
        sponsor = item.sponsor
        lines.append(
            "| "
            f"{item.score:.2f} | "
            f"{escape_markdown_cell(item.match_type)} | "
            f"{escape_markdown_cell(offer.get('company'))} | "
            f"{escape_markdown_cell(offer.get('title'))} | "
            f"{escape_markdown_cell(offer.get('location'))} | "
            f"{escape_markdown_cell(offer.get('source'))} | "
            f"{escape_markdown_cell(sponsor.get('organisation_name'))} | "
            f"{escape_markdown_cell(sponsor.get('town_city'))} | "
            f"{escape_markdown_cell(sponsor.get('route'))} | "
            f"{escape_markdown_cell(offer.get('url'))} |"
        )

    if not matches:
        lines.append("| No matches |  |  |  |  |  |  |  |  |  |")

    lines.append("")
    return "\n".join(lines)


def render_matched_json_payload(
    matches: list[MatchRecord],
    jobs_payload: dict[str, Any],
    sponsors_payload: dict[str, Any],
    generated_at: str,
) -> dict[str, Any]:
    return {
        "metadata": {
            "generated_at": generated_at,
            "job_offers_fetched": jobs_payload.get("metadata", {}).get(
                "total_offers", 0
            ),
            "sponsors_fetched": sponsors_payload.get("metadata", {}).get(
                "total_sponsors", 0
            ),
            "matched_rows": len(matches),
            "locations": jobs_payload.get("metadata", {}).get("locations", []),
        },
        "matches": [
            {
                "match_score": item.score,
                "match_type": item.match_type,
                "offer": item.offer,
                "sponsor": item.sponsor,
            }
            for item in matches
        ],
    }


def build_report_artifacts(request: ReportRequest) -> ReportArtifacts:
    jobs_payload = build_job_offers_payload(
        JobOffersRequest(
            keywords=request.keywords,
            location=request.location,
            locations=request.locations,
            locations_file=request.locations_file,
            page=request.page,
            results_per_page=request.results_per_page,
            sources=request.sources,
            config_path=request.config_path,
            timeout=request.job_timeout,
            single_page=request.single_page,
            max_pages=request.max_pages,
        )
    )
    sponsors_payload = build_sponsors_payload(
        SponsorsRequest(timeout=request.sponsor_timeout)
    )

    offers = cast(list[dict[str, Any]], jobs_payload.get("offers", []))
    sponsors = cast(list[dict[str, str]], sponsors_payload.get("sponsors", []))
    matches = match_offers_with_sponsors(offers, sponsors)
    generated_at = datetime.now(timezone.utc).isoformat()
    markdown = render_markdown(matches, jobs_payload, sponsors_payload, generated_at)
    hugo_markdown = render_hugo_content(markdown, generated_at)
    matched_payload = render_matched_json_payload(
        matches=matches,
        jobs_payload=jobs_payload,
        sponsors_payload=sponsors_payload,
        generated_at=generated_at,
    )

    return ReportArtifacts(
        generated_at=generated_at,
        jobs_payload=jobs_payload,
        sponsors_payload=sponsors_payload,
        matches=matches,
        markdown=markdown,
        hugo_markdown=hugo_markdown,
        matched_payload=matched_payload,
    )
