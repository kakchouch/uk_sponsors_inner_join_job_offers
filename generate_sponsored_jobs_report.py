from __future__ import annotations

import argparse
from pathlib import Path
from uk_sponsors.json_io import write_json, write_text
from uk_sponsors.output_paths import (
    DEFAULT_JOBS_OUTPUT,
    DEFAULT_MARKDOWN_OUTPUT,
    DEFAULT_MATCHED_JSON_OUTPUT,
    DEFAULT_SITE_REPORT_OUTPUT,
    DEFAULT_SPONSORS_OUTPUT,
)
from uk_sponsors.reporting import ReportRequest, build_report_artifacts


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
    parser.add_argument(
        "--locations",
        nargs="*",
        default=[],
        help=(
            "Optional list of locations to fetch separately and merge into one report. "
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
    parser.add_argument(
        "--sources",
        nargs="*",
        default=[],
        help=(
            "Optional list of source ids and/or numeric source indexes "
            "from input/job_sources.json (example: --sources adzuna 2)."
        ),
    )
    parser.add_argument(
        "--exclude-sources",
        nargs="*",
        default=[],
        help=(
            "Optional list of source ids and/or numeric source indexes to skip. "
            "Excluded sources are not queried."
        ),
    )
    parser.add_argument("--jobs-output", default=str(DEFAULT_JOBS_OUTPUT))
    parser.add_argument("--sponsors-output", default=str(DEFAULT_SPONSORS_OUTPUT))
    parser.add_argument("--markdown-output", default=str(DEFAULT_MARKDOWN_OUTPUT))
    parser.add_argument(
        "--site-report-output",
        default=str(DEFAULT_SITE_REPORT_OUTPUT),
        help=(
            "Optional path to write the Hugo-formatted content page (frontmatter + "
            "report body). Example: output/site/content/report.md"
        ),
    )
    parser.add_argument(
        "--matched-json-output",
        default=str(DEFAULT_MATCHED_JSON_OUTPUT),
        help=(
            "Optional output path for matched records JSON. "
            f"Example: {DEFAULT_MATCHED_JSON_OUTPUT}"
        ),
    )
    parser.add_argument("--job-timeout", type=int, default=20)
    parser.add_argument("--sponsor-timeout", type=int, default=30)
    parser.add_argument("--config", default="input/job_sources.json")
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
    artifacts = build_report_artifacts(
        ReportRequest(
            keywords=args.keywords,
            location=args.location,
            locations=tuple(args.locations),
            locations_file=args.locations_file,
            page=args.page,
            results_per_page=args.results_per_page,
            sources=tuple(args.sources),
            excluded_sources=tuple(args.exclude_sources),
            config_path=Path(args.config),
            job_timeout=args.job_timeout,
            sponsor_timeout=args.sponsor_timeout,
            single_page=args.single_page,
            max_pages=args.max_pages,
        )
    )

    write_json(Path(args.jobs_output), artifacts.jobs_payload)
    write_json(Path(args.sponsors_output), artifacts.sponsors_payload)
    write_text(Path(args.markdown_output), artifacts.markdown)

    if args.site_report_output:
        site_path = Path(args.site_report_output)
        write_text(site_path, artifacts.hugo_markdown)
        print(f"Hugo content written to: {site_path}")

    if args.matched_json_output:
        matched_json_path = Path(args.matched_json_output)
        write_json(matched_json_path, artifacts.matched_payload)
        print(f"Matched JSON written to: {matched_json_path}")

    print(f"Matched rows: {len(artifacts.matches)}")
    print(f"Markdown report written to: {args.markdown_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
