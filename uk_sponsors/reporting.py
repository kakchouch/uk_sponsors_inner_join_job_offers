from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .job_offers import DEFAULT_CONFIG_PATH, JobOffersRequest, build_job_offers_payload
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


@dataclass(frozen=True)
class MatchRecord:
    offer: dict[str, Any]
    sponsor: dict[str, str]


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


def build_sponsor_indexes(
    sponsors: list[dict[str, str]],
) -> tuple[dict[str, list[dict[str, str]]], dict[str, set[int]], list[str]]:
    by_name: dict[str, list[dict[str, str]]] = defaultdict(list)
    token_to_indices: dict[str, set[int]] = defaultdict(set)
    normalized_names: list[str] = []

    for index, sponsor in enumerate(sponsors):
        normalized = normalize_company_name(sponsor.get("organisation_name", ""))
        normalized_names.append(normalized)
        if normalized:
            by_name[normalized].append(sponsor)

        for token in set(normalized.split()):
            if len(token) >= 3:
                token_to_indices[token].add(index)

    return by_name, token_to_indices, normalized_names


def is_partial_match(company_normalized: str, sponsor_normalized: str) -> bool:
    if not company_normalized or not sponsor_normalized:
        return False

    if company_normalized in sponsor_normalized and len(company_normalized) >= 6:
        return True

    if sponsor_normalized in company_normalized and len(sponsor_normalized) >= 6:
        return True

    return False


def match_offers_with_sponsors(
    offers: list[dict[str, Any]],
    sponsors: list[dict[str, str]],
) -> list[MatchRecord]:
    by_name, token_to_indices, normalized_sponsor_names = build_sponsor_indexes(
        sponsors
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
                matches.append(MatchRecord(offer=offer, sponsor=sponsor))
            continue

        candidate_indices: set[int] = set()
        for token in set(company_normalized.split()):
            candidate_indices.update(token_to_indices.get(token, set()))

        for index in candidate_indices:
            sponsor_normalized = normalized_sponsor_names[index]
            if is_partial_match(company_normalized, sponsor_normalized):
                matches.append(MatchRecord(offer=offer, sponsor=sponsors[index]))

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
            "| Company | Job Title | Location | Source | Sponsor Town/City | Route | Job URL |",
            "|---|---|---|---|---|---|---|",
        ]
    )

    for item in matches:
        offer = item.offer
        sponsor = item.sponsor
        lines.append(
            "| "
            f"{escape_markdown_cell(offer.get('company'))} | "
            f"{escape_markdown_cell(offer.get('title'))} | "
            f"{escape_markdown_cell(offer.get('location'))} | "
            f"{escape_markdown_cell(offer.get('source'))} | "
            f"{escape_markdown_cell(sponsor.get('town_city'))} | "
            f"{escape_markdown_cell(sponsor.get('route'))} | "
            f"{escape_markdown_cell(offer.get('url'))} |"
        )

    if not matches:
        lines.append("| No matches |  |  |  |  |  |  |")

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

    offers = jobs_payload.get("offers", [])
    sponsors = sponsors_payload.get("sponsors", [])
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
