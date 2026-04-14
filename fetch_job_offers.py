from __future__ import annotations

import argparse
import base64
import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

DEFAULT_CONFIG_PATH = Path("job_sources.json")
DEFAULT_OUTPUT_PATH = Path("job_offers.json")


@dataclass(frozen=True)
class SourceConfig:
    id: str
    name: str
    enabled: bool
    base_url: str
    results_per_page: int
    auth: dict[str, Any]
    query_defaults: dict[str, Any]
    country: str | None = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch job offers from configured public APIs and export a normalized JSON file."
        )
    )
    parser.add_argument("--keywords", default="software engineer")
    parser.add_argument("--location", default="United Kingdom")
    parser.add_argument("--page", type=int, default=1)
    parser.add_argument("--results-per-page", type=int, default=20)
    parser.add_argument("--sources", nargs="*", default=[])
    parser.add_argument("--config", default=str(DEFAULT_CONFIG_PATH))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT_PATH))
    parser.add_argument("--timeout", type=int, default=20)
    return parser.parse_args()


def load_sources(config_path: Path) -> list[SourceConfig]:
    with config_path.open("r", encoding="utf-8") as handle:
        raw = json.load(handle)

    sources: list[SourceConfig] = []
    for item in raw.get("sources", []):
        sources.append(
            SourceConfig(
                id=item["id"],
                name=item["name"],
                enabled=item.get("enabled", True),
                base_url=item["base_url"],
                country=item.get("country"),
                results_per_page=item.get("results_per_page", 20),
                auth=item.get("auth", {}),
                query_defaults=item.get("query_defaults", {}),
            )
        )
    return sources


def resolve_auth(source: SourceConfig) -> tuple[dict[str, str], dict[str, str]]:
    headers: dict[str, str] = {}
    query_params: dict[str, str] = {}

    auth_type = source.auth.get("type", "none")
    required_env = source.auth.get("required_env", [])

    env_values = {}
    missing = []
    for env_name in required_env:
        value = os.getenv(env_name)
        if value:
            env_values[env_name] = value
        else:
            missing.append(env_name)

    if missing:
        missing_str = ", ".join(missing)
        raise RuntimeError(
            f"Missing required environment variables for {source.id}: {missing_str}"
        )

    if auth_type == "query":
        mappings = source.auth.get("mappings", {})
        for env_name, param_name in mappings.items():
            query_params[param_name] = env_values[env_name]

    if auth_type == "basic_api_key":
        key_name = required_env[0]
        token = base64.b64encode(f"{env_values[key_name]}:".encode("utf-8")).decode(
            "utf-8"
        )
        headers["Authorization"] = f"Basic {token}"

    return headers, query_params


def fetch_source_offers(
    source: SourceConfig, args: argparse.Namespace, session: requests.Session
) -> list[dict[str, Any]]:
    headers, auth_params = resolve_auth(source)

    if source.id == "adzuna":
        return fetch_adzuna(source, args, session, headers, auth_params)

    if source.id == "reed":
        return fetch_reed(source, args, session, headers, auth_params)

    raise ValueError(f"Unsupported source id: {source.id}")


def fetch_adzuna(
    source: SourceConfig,
    args: argparse.Namespace,
    session: requests.Session,
    headers: dict[str, str],
    auth_params: dict[str, str],
) -> list[dict[str, Any]]:
    endpoint = f"{source.base_url}/{source.country}/search/{args.page}"
    params = dict(source.query_defaults)
    params.update(
        {
            "what": args.keywords,
            "where": args.location,
            "results_per_page": min(args.results_per_page, 50),
        }
    )
    params.update(auth_params)

    response = session.get(
        endpoint, params=params, headers=headers, timeout=args.timeout
    )
    response.raise_for_status()

    payload = response.json()
    items = payload.get("results", [])
    return [normalize_adzuna_item(item, source.id) for item in items]


def fetch_reed(
    source: SourceConfig,
    args: argparse.Namespace,
    session: requests.Session,
    headers: dict[str, str],
    auth_params: dict[str, str],
) -> list[dict[str, Any]]:
    endpoint = f"{source.base_url}/search"
    params = dict(source.query_defaults)
    params.update(
        {
            "keywords": args.keywords,
            "locationName": args.location,
            "resultsToTake": min(args.results_per_page, 100),
            "resultsToSkip": max(args.page - 1, 0) * args.results_per_page,
        }
    )
    params.update(auth_params)

    response = session.get(
        endpoint, params=params, headers=headers, timeout=args.timeout
    )
    response.raise_for_status()

    payload = response.json()
    items = payload.get("results", [])
    return [normalize_reed_item(item, source.id) for item in items]


def normalize_adzuna_item(item: dict[str, Any], source_id: str) -> dict[str, Any]:
    company = item.get("company") or {}
    location = item.get("location") or {}

    return {
        "source": source_id,
        "external_id": item.get("id"),
        "title": item.get("title"),
        "company": company.get("display_name"),
        "location": location.get("display_name"),
        "salary_min": item.get("salary_min"),
        "salary_max": item.get("salary_max"),
        "currency": "GBP",
        "contract_type": item.get("contract_type"),
        "contract_time": item.get("contract_time"),
        "posted_at": item.get("created"),
        "url": item.get("redirect_url"),
        "raw": item,
    }


def normalize_reed_item(item: dict[str, Any], source_id: str) -> dict[str, Any]:
    return {
        "source": source_id,
        "external_id": item.get("jobId"),
        "title": item.get("jobTitle"),
        "company": item.get("employerName"),
        "location": item.get("locationName"),
        "salary_min": item.get("minimumSalary"),
        "salary_max": item.get("maximumSalary"),
        "currency": "GBP",
        "contract_type": item.get("jobType"),
        "contract_time": None,
        "posted_at": item.get("date"),
        "url": item.get("jobUrl"),
        "raw": item,
    }


def select_sources(
    all_sources: list[SourceConfig], requested_sources: list[str]
) -> list[SourceConfig]:
    enabled_sources = [item for item in all_sources if item.enabled]
    if not requested_sources:
        return enabled_sources

    requested_set = {item.strip().lower() for item in requested_sources}
    return [item for item in enabled_sources if item.id.lower() in requested_set]


def export_offers(
    output_path: Path,
    offers: list[dict[str, Any]],
    sources_used: list[str],
    keywords: str,
    location: str,
) -> None:
    output = {
        "metadata": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "sources": sources_used,
            "keywords": keywords,
            "location": location,
            "total_offers": len(offers),
        },
        "offers": offers,
    }

    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(output, handle, indent=2, ensure_ascii=False)


def main() -> int:
    args = parse_args()
    sources = load_sources(Path(args.config))
    selected_sources = select_sources(sources, args.sources)

    if not selected_sources:
        raise RuntimeError(
            "No enabled source selected. Check --sources value and job_sources.json."
        )

    offers: list[dict[str, Any]] = []
    used_sources: list[str] = []

    with requests.Session() as session:
        for source in selected_sources:
            source_offers = fetch_source_offers(source, args, session)
            offers.extend(source_offers)
            used_sources.append(source.id)

    export_offers(
        output_path=Path(args.output),
        offers=offers,
        sources_used=used_sources,
        keywords=args.keywords,
        location=args.location,
    )

    print(f"Fetched {len(offers)} offers from {', '.join(used_sources)}")
    print(f"Output written to: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
