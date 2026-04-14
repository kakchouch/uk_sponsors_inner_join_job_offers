from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from urllib.parse import urljoin

import requests

DEFAULT_PUBLICATION_URL = (
    "https://www.gov.uk/government/publications/"
    "register-of-licensed-sponsors-workers"
)


@dataclass(frozen=True)
class SponsorsRequest:
    page_url: str = DEFAULT_PUBLICATION_URL
    timeout: int = 30


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


def build_sponsors_payload(request: SponsorsRequest) -> dict[str, object]:
    csv_url = discover_csv_url(request.page_url, request.timeout)
    sponsors, headers = download_csv_rows(csv_url, request.timeout)

    return {
        "metadata": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "source_page_url": request.page_url,
            "source_csv_url": csv_url,
            "total_sponsors": len(sponsors),
            "original_csv_headers": headers,
        },
        "sponsors": sponsors,
    }
