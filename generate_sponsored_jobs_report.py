from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_JOBS_OUTPUT = Path("tmp_job_offers.json")
DEFAULT_SPONSORS_OUTPUT = Path("tmp_registered_sponsors.json")
DEFAULT_MARKDOWN_OUTPUT = Path("sponsored_jobs_report.md")
DEFAULT_MATCHED_JSON_OUTPUT = Path("matched_sponsored_jobs.json")

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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run both fetch scripts, match job offers with registered sponsors, and "
            "export a Markdown report."
        )
    )
    parser.add_argument(
        "--keywords",
        default="",
        help="Optional keywords filter. Leave empty to scan all job types.",
    )
    parser.add_argument(
        "--location",
        default="",
        help="Optional location filter. Leave empty to avoid location filtering.",
    )
    parser.add_argument("--page", type=int, default=1)
    parser.add_argument("--results-per-page", type=int, default=20)
    parser.add_argument("--sources", nargs="*", default=[])
    parser.add_argument("--jobs-output", default=str(DEFAULT_JOBS_OUTPUT))
    parser.add_argument("--sponsors-output", default=str(DEFAULT_SPONSORS_OUTPUT))
    parser.add_argument("--markdown-output", default=str(DEFAULT_MARKDOWN_OUTPUT))
    parser.add_argument(
        "--matched-json-output",
        default=None,
        help=(
            "Optional output path for matched records JSON. "
            f"Example: {DEFAULT_MATCHED_JSON_OUTPUT}"
        ),
    )
    parser.add_argument("--job-timeout", type=int, default=20)
    parser.add_argument("--sponsor-timeout", type=int, default=30)
    return parser.parse_args()


def run_job_fetch(args: argparse.Namespace) -> None:
    command = [
        sys.executable,
        "fetch_job_offers.py",
        "--keywords",
        args.keywords,
        "--location",
        args.location,
        "--page",
        str(args.page),
        "--results-per-page",
        str(args.results_per_page),
        "--output",
        args.jobs_output,
        "--timeout",
        str(args.job_timeout),
    ]
    if args.sources:
        command.extend(["--sources", *args.sources])

    subprocess.run(command, check=True)


def run_sponsor_fetch(args: argparse.Namespace) -> None:
    command = [
        sys.executable,
        "fetch_registered_sponsors.py",
        "--output",
        args.sponsors_output,
        "--timeout",
        str(args.sponsor_timeout),
    ]
    subprocess.run(command, check=True)


def load_payload(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data: dict[str, Any] = json.load(handle)
    return data


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


def render_markdown(
    matches: list[MatchRecord],
    jobs_payload: dict[str, Any],
    sponsors_payload: dict[str, Any],
) -> str:
    generated_at = datetime.now(timezone.utc).isoformat()
    jobs_meta = jobs_payload.get("metadata", {})
    sponsors_meta = sponsors_payload.get("metadata", {})

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
        "",
        "## Matches",
        "",
        "| Company | Job Title | Location | Source | Sponsor Town/City | Route | Job URL |",
        "|---|---|---|---|---|---|---|",
    ]

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
) -> dict[str, Any]:
    return {
        "metadata": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "job_offers_fetched": jobs_payload.get("metadata", {}).get(
                "total_offers", 0
            ),
            "sponsors_fetched": sponsors_payload.get("metadata", {}).get(
                "total_sponsors", 0
            ),
            "matched_rows": len(matches),
        },
        "matches": [
            {
                "offer": item.offer,
                "sponsor": item.sponsor,
            }
            for item in matches
        ],
    }


def main() -> int:
    args = parse_args()

    run_job_fetch(args)
    run_sponsor_fetch(args)

    jobs_payload = load_payload(Path(args.jobs_output))
    sponsors_payload = load_payload(Path(args.sponsors_output))

    offers = jobs_payload.get("offers", [])
    sponsors = sponsors_payload.get("sponsors", [])

    matches = match_offers_with_sponsors(offers, sponsors)
    markdown = render_markdown(matches, jobs_payload, sponsors_payload)

    output_path = Path(args.markdown_output)
    output_path.write_text(markdown, encoding="utf-8")

    if args.matched_json_output:
        matched_json_path = Path(args.matched_json_output)
        matched_payload = render_matched_json_payload(
            matches=matches,
            jobs_payload=jobs_payload,
            sponsors_payload=sponsors_payload,
        )
        with matched_json_path.open("w", encoding="utf-8") as handle:
            json.dump(matched_payload, handle, indent=2, ensure_ascii=False)
        print(f"Matched JSON written to: {matched_json_path}")

    print(f"Matched rows: {len(matches)}")
    print(f"Markdown report written to: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
