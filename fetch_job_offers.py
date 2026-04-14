from __future__ import annotations

import argparse
from pathlib import Path
from uk_sponsors.job_offers import (
    DEFAULT_CONFIG_PATH,
    JobOffersRequest,
    build_job_offers_payload,
)
from uk_sponsors.json_io import write_json
from uk_sponsors.output_paths import DEFAULT_JOBS_OUTPUT


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch job offers from configured public APIs and export a normalized JSON file."
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
    parser.add_argument(
        "--locations",
        nargs="*",
        default=[],
        help=(
            "Optional list of locations to fetch separately and merge into one output. "
            "Takes precedence over --location."
        ),
    )
    parser.add_argument(
        "--locations-file",
        default="",
        help=(
            "Optional JSON file containing a 'locations' array. "
            "Takes precedence over --locations and --location."
        ),
    )
    parser.add_argument("--page", type=int, default=1)
    parser.add_argument("--results-per-page", type=int, default=20)
    parser.add_argument("--sources", nargs="*", default=[])
    parser.add_argument("--config", default=str(DEFAULT_CONFIG_PATH))
    parser.add_argument("--output", default=str(DEFAULT_JOBS_OUTPUT))
    parser.add_argument("--timeout", type=int, default=20)
    parser.add_argument(
        "--single-page",
        action="store_true",
        help="Fetch only one page per source (keeps legacy behavior).",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=0,
        help=(
            "Optional cap on pages fetched per source when not using --single-page. "
            "0 means no cap."
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payload = build_job_offers_payload(
        JobOffersRequest(
            keywords=args.keywords,
            location=args.location,
            locations=tuple(args.locations),
            locations_file=args.locations_file,
            page=args.page,
            results_per_page=args.results_per_page,
            sources=tuple(args.sources),
            config_path=Path(args.config),
            timeout=args.timeout,
            single_page=args.single_page,
            max_pages=args.max_pages,
        )
    )
    write_json(Path(args.output), payload)

    used_sources = payload.get("metadata", {}).get("sources", [])
    offers = payload.get("offers", [])
    print(f"Fetched {len(offers)} offers from {', '.join(used_sources)}")
    print(f"Output written to: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
