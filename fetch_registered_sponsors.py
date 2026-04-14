from __future__ import annotations

import argparse
from pathlib import Path
from uk_sponsors.json_io import write_json
from uk_sponsors.output_paths import DEFAULT_SPONSORS_OUTPUT
from uk_sponsors.registered_sponsors import (
    DEFAULT_PUBLICATION_URL,
    SponsorsRequest,
    build_sponsors_payload,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch the latest UK registered worker sponsors CSV from GOV.UK and "
            "export normalized JSON."
        )
    )
    parser.add_argument("--page-url", default=DEFAULT_PUBLICATION_URL)
    parser.add_argument("--output", default=str(DEFAULT_SPONSORS_OUTPUT))
    parser.add_argument("--timeout", type=int, default=30)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payload = build_sponsors_payload(
        SponsorsRequest(page_url=args.page_url, timeout=args.timeout)
    )
    write_json(Path(args.output), payload)

    print(f"Fetched {len(payload.get('sponsors', []))} sponsors")
    print(f"Source CSV: {payload.get('metadata', {}).get('source_csv_url', '')}")
    print(f"Output written to: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
