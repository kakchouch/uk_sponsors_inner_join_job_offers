from __future__ import annotations

import argparse
from pathlib import Path

from uk_sponsors.analytics import (
    DEFAULT_CHARTS_OUTPUT_DIR,
    DEFAULT_MARKET_ANALYTICS_MARKDOWN_OUTPUT,
    DEFAULT_MARKET_ANALYTICS_OUTPUT,
    DEFAULT_SITE_ANALYTICS_OUTPUT,
    save_market_analytics_outputs,
)
from uk_sponsors.json_io import read_json


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate deduplicated market analytics, charts, and site content "
            "from the matched sponsored jobs payload."
        )
    )
    parser.add_argument(
        "--matched-json-input",
        default="output/reports/matched_sponsored_jobs.json",
        help="Path to the matched sponsored jobs JSON payload.",
    )
    parser.add_argument(
        "--keywords",
        default="",
        help="Optional keyword filter description to include in the analytics report.",
    )
    parser.add_argument(
        "--json-output",
        default=str(DEFAULT_MARKET_ANALYTICS_OUTPUT),
        help="Output path for market analytics JSON.",
    )
    parser.add_argument(
        "--markdown-output",
        default=str(DEFAULT_MARKET_ANALYTICS_MARKDOWN_OUTPUT),
        help="Output path for the markdown analytics report.",
    )
    parser.add_argument(
        "--site-markdown-output",
        default=str(DEFAULT_SITE_ANALYTICS_OUTPUT),
        help="Output path for the Hugo-ready analytics page.",
    )
    parser.add_argument(
        "--charts-output-dir",
        default=str(DEFAULT_CHARTS_OUTPUT_DIR),
        help="Directory where PNG analytics charts are written.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    matches = read_json(Path(args.matched_json_input))
    analytics = save_market_analytics_outputs(
        matches,
        json_output_path=Path(args.json_output),
        markdown_output_path=Path(args.markdown_output),
        site_markdown_output_path=Path(args.site_markdown_output),
        charts_output_dir=Path(args.charts_output_dir),
        keywords=args.keywords,
    )

    print(f"Analytics JSON written to: {args.json_output}")
    print(f"Analytics markdown written to: {args.markdown_output}")
    print(f"Analytics site page written to: {args.site_markdown_output}")
    print(f"Charts written to: {args.charts_output_dir}")
    print(f"Unique matched jobs: {analytics['overview']['matched_jobs']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
