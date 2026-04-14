from __future__ import annotations

import argparse
import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import requests

DEFAULT_PUBLICATION_URL = (
    "https://www.gov.uk/government/publications/"
    "register-of-licensed-sponsors-workers"
)
DEFAULT_OUTPUT_PATH = Path("registered_sponsors.json")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch the latest UK registered worker sponsors CSV from GOV.UK and "
            "export normalized JSON."
        )
    )
    parser.add_argument("--page-url", default=DEFAULT_PUBLICATION_URL)
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT_PATH))
    parser.add_argument("--timeout", type=int, default=30)
    return parser.parse_args()


def to_snake_case(value: str) -> str:
    cleaned = re.sub(r"[^0-9a-zA-Z]+", "_", value.strip().lower())
    return cleaned.strip("_")


def discover_csv_url(page_url: str, timeout: int) -> str:
    response = requests.get(page_url, timeout=timeout)
    response.raise_for_status()
    html = response.text

    hrefs = re.findall(r'href=["\']([^"\']+)["\']', html, flags=re.IGNORECASE)
    csv_links: list[str] = []

    for href in hrefs:
        absolute_url = urljoin(page_url, href)
        if absolute_url.lower().endswith(".csv"):
            csv_links.append(absolute_url)

    worker_links = [
        item
        for item in csv_links
        if "worker_and_temporary_worker" in item.lower()
        or "licensed-sponsors-workers" in item.lower()
    ]

    selected = (
        worker_links[0] if worker_links else (csv_links[0] if csv_links else None)
    )
    if not selected:
        raise RuntimeError("Could not find a CSV link on the GOV.UK publication page.")

    return selected


def download_csv_rows(
    csv_url: str, timeout: int
) -> tuple[list[dict[str, str]], list[str]]:
    response = requests.get(csv_url, timeout=timeout)
    response.raise_for_status()

    content = response.content.decode("utf-8-sig", errors="replace")
    reader = csv.DictReader(content.splitlines())
    original_headers = list(reader.fieldnames or [])

    rows: list[dict[str, str]] = []
    for row in reader:
        normalized_row: dict[str, str] = {}
        for header in original_headers:
            normalized_key = to_snake_case(header)
            normalized_row[normalized_key] = (row.get(header) or "").strip()
        rows.append(normalized_row)

    return rows, original_headers


def export_sponsors_json(
    output_path: Path,
    sponsors: list[dict[str, str]],
    source_page_url: str,
    source_csv_url: str,
    original_headers: list[str],
) -> None:
    payload: dict[str, Any] = {
        "metadata": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "source_page_url": source_page_url,
            "source_csv_url": source_csv_url,
            "total_sponsors": len(sponsors),
            "original_csv_headers": original_headers,
        },
        "sponsors": sponsors,
    }

    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)


def main() -> int:
    args = parse_args()

    csv_url = discover_csv_url(args.page_url, args.timeout)
    sponsors, headers = download_csv_rows(csv_url, args.timeout)

    export_sponsors_json(
        output_path=Path(args.output),
        sponsors=sponsors,
        source_page_url=args.page_url,
        source_csv_url=csv_url,
        original_headers=headers,
    )

    print(f"Fetched {len(sponsors)} sponsors")
    print(f"Source CSV: {csv_url}")
    print(f"Output written to: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
