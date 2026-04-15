from __future__ import annotations

import base64
import json
import logging
import os
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from math import ceil
from pathlib import Path
from typing import Any

import requests

DEFAULT_CONFIG_PATH = Path("input/job_sources.json")
LOGGER = logging.getLogger(__name__)
TRANSIENT_HTTP_STATUS_CODES = {429, 500, 502, 503, 504}
MAX_FETCH_RETRIES = 3
RETRY_BACKOFF_SECONDS = 1.5


@dataclass(frozen=True)
class SourceConfig:
    index: int
    id: str
    name: str
    enabled: bool
    base_url: str
    results_per_page: int
    auth: dict[str, Any]
    query_defaults: dict[str, Any]
    country: str | None = None


@dataclass(frozen=True)
class JobOffersRequest:
    keywords: str = ""
    location: str = ""
    locations: tuple[str, ...] = ()
    locations_file: str = ""
    page: int = 1
    results_per_page: int = 20
    sources: tuple[str, ...] = ()
    excluded_sources: tuple[str, ...] = ()
    config_path: Path = DEFAULT_CONFIG_PATH
    timeout: int = 20
    single_page: bool = False
    max_pages: int = 0


def parse_locations(location: str, locations: list[str]) -> list[str]:
    parsed_locations = [item.strip() for item in locations if item.strip()]
    if parsed_locations:
        return parsed_locations

    if location.strip():
        return [location.strip()]

    return []


def load_locations_file(locations_file: str) -> list[str]:
    if not locations_file:
        return []

    with Path(locations_file).open("r", encoding="utf-8") as handle:
        payload = json.load(handle)

    raw_locations = payload.get("locations", [])
    if not isinstance(raw_locations, list):
        raise ValueError("Locations file must contain a 'locations' list.")

    return [str(item).strip() for item in raw_locations if str(item).strip()]


def resolve_locations(
    location: str, locations: list[str], locations_file: str
) -> list[str]:
    file_locations = load_locations_file(locations_file)
    if file_locations:
        return file_locations

    return parse_locations(location, locations)


def deduplicate_offers(offers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    deduplicated: list[dict[str, Any]] = []
    seen_keys: set[tuple[str, str, str, str, str, str]] = set()

    for offer in offers:
        dedupe_key = (
            str(offer.get("source") or ""),
            str(offer.get("external_id") or ""),
            str(offer.get("url") or ""),
            str(offer.get("title") or ""),
            str(offer.get("company") or ""),
            str(offer.get("location") or ""),
        )
        if dedupe_key in seen_keys:
            continue

        seen_keys.add(dedupe_key)
        deduplicated.append(offer)

    return deduplicated


def filter_offers_by_locations(
    offers: list[dict[str, Any]], locations: list[str]
) -> list[dict[str, Any]]:
    lowered = [loc.lower() for loc in locations]
    return [
        offer
        for offer in offers
        if any(loc in (offer.get("location") or "").lower() for loc in lowered)
    ]


def load_sources(config_path: Path) -> list[SourceConfig]:
    with config_path.open("r", encoding="utf-8") as handle:
        raw = json.load(handle)

    sources: list[SourceConfig] = []
    for index, item in enumerate(raw.get("sources", []), start=1):
        sources.append(
            SourceConfig(
                index=index,
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


def fetch_json_with_retry(
    session: requests.Session,
    endpoint: str,
    *,
    params: dict[str, Any],
    headers: dict[str, str],
    timeout: int,
    source_id: str,
    page_number: int,
) -> dict[str, Any]:
    for attempt in range(1, MAX_FETCH_RETRIES + 1):
        try:
            response = session.get(
                endpoint,
                params=params,
                headers=headers,
                timeout=timeout,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            status_code = getattr(getattr(error, "response", None), "status_code", None)
            is_transient_http = status_code in TRANSIENT_HTTP_STATUS_CODES
            is_transport_error = isinstance(
                error,
                (
                    requests.exceptions.ConnectionError,
                    requests.exceptions.Timeout,
                ),
            )
            should_retry = attempt < MAX_FETCH_RETRIES and (
                is_transient_http or is_transport_error
            )
            if not should_retry:
                raise

            delay_seconds = RETRY_BACKOFF_SECONDS * attempt
            LOGGER.warning(
                "Retrying %s page %s after attempt %s failed with %s",
                source_id,
                page_number,
                attempt,
                status_code or error.__class__.__name__,
            )
            time.sleep(delay_seconds)

    raise RuntimeError(
        f"Exhausted retries while fetching {source_id} page {page_number}."
    )


def fetch_source_offers(
    source: SourceConfig,
    request: JobOffersRequest,
    session: requests.Session,
    locations: list[str],
) -> list[dict[str, Any]]:
    headers, auth_params = resolve_auth(source)

    # When multiple cities are requested, fetch UK-wide once and post-filter
    # locally. This reduces N_cities × N_pages API calls to N_pages.
    locations_to_fetch = [""] if len(locations) > 1 else (locations or [""])
    offers: list[dict[str, Any]] = []

    for location in locations_to_fetch:
        if source.id == "adzuna":
            offers.extend(
                fetch_adzuna(source, request, session, headers, auth_params, location)
            )
            continue

        if source.id == "reed":
            offers.extend(
                fetch_reed(source, request, session, headers, auth_params, location)
            )
            continue

        raise ValueError(f"Unsupported source id: {source.id}")

    if len(locations) > 1:
        offers = filter_offers_by_locations(offers, locations)

    return deduplicate_offers(offers)


def fetch_adzuna(
    source: SourceConfig,
    request: JobOffersRequest,
    session: requests.Session,
    headers: dict[str, str],
    auth_params: dict[str, str],
    location: str,
) -> list[dict[str, Any]]:
    per_page = min(request.results_per_page, 50)
    params = dict(source.query_defaults)
    params["results_per_page"] = per_page
    if request.keywords.strip():
        params["what"] = request.keywords.strip()
    else:
        params.pop("what", None)
    if location.strip():
        params["where"] = location.strip()
    else:
        params.pop("where", None)
    params.update(auth_params)

    def fetch_page(page_number: int) -> dict[str, Any]:
        endpoint = f"{source.base_url}/{source.country}/search/{page_number}"
        return fetch_json_with_retry(
            session,
            endpoint,
            params=params,
            headers=headers,
            timeout=request.timeout,
            source_id=source.id,
            page_number=page_number,
        )

    first_payload = fetch_page(request.page)
    first_items = first_payload.get("results", [])
    offers = [normalize_adzuna_item(item, source.id) for item in first_items]

    if request.single_page:
        return offers

    total_count = int(first_payload.get("count", 0) or 0)
    total_pages = ceil(total_count / per_page) if per_page else 0
    if total_pages <= request.page:
        return offers

    page_cap = total_pages
    if request.max_pages > 0:
        page_cap = min(page_cap, request.page + request.max_pages - 1)

    for page_number in range(request.page + 1, page_cap + 1):
        try:
            payload = fetch_page(page_number)
        except requests.exceptions.RequestException as error:
            LOGGER.warning(
                "Stopping %s pagination at page %s after repeated fetch failures: %s",
                source.id,
                page_number,
                error,
            )
            break
        items = payload.get("results", [])
        if not items:
            break
        offers.extend(normalize_adzuna_item(item, source.id) for item in items)

    return offers


def fetch_reed(
    source: SourceConfig,
    request: JobOffersRequest,
    session: requests.Session,
    headers: dict[str, str],
    auth_params: dict[str, str],
    location: str,
) -> list[dict[str, Any]]:
    endpoint = f"{source.base_url}/search"
    per_page = min(request.results_per_page, 100)
    base_params = dict(source.query_defaults)
    base_params["resultsToTake"] = per_page
    if request.keywords.strip():
        base_params["keywords"] = request.keywords.strip()
    else:
        base_params.pop("keywords", None)
    if location.strip():
        base_params["locationName"] = location.strip()
    else:
        base_params.pop("locationName", None)
    base_params.update(auth_params)

    def fetch_page(page_number: int) -> dict[str, Any]:
        params = dict(base_params)
        params["resultsToSkip"] = max(page_number - 1, 0) * per_page
        return fetch_json_with_retry(
            session,
            endpoint,
            params=params,
            headers=headers,
            timeout=request.timeout,
            source_id=source.id,
            page_number=page_number,
        )

    first_payload = fetch_page(request.page)
    first_items = first_payload.get("results", [])
    offers = [normalize_reed_item(item, source.id) for item in first_items]

    if request.single_page:
        return offers

    total_count = int(first_payload.get("totalResults", 0) or 0)
    total_pages = ceil(total_count / per_page) if per_page else 0
    if total_pages <= request.page:
        return offers

    page_cap = total_pages
    if request.max_pages > 0:
        page_cap = min(page_cap, request.page + request.max_pages - 1)

    for page_number in range(request.page + 1, page_cap + 1):
        try:
            payload = fetch_page(page_number)
        except requests.exceptions.RequestException as error:
            LOGGER.warning(
                "Stopping %s pagination at page %s after repeated fetch failures: %s",
                source.id,
                page_number,
                error,
            )
            break
        items = payload.get("results", [])
        if not items:
            break
        offers.extend(normalize_reed_item(item, source.id) for item in items)

    return offers


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
    all_sources: list[SourceConfig],
    requested_sources: tuple[str, ...],
    excluded_sources: tuple[str, ...],
) -> list[SourceConfig]:
    def to_selector_set(values: tuple[str, ...]) -> set[str]:
        return {item.strip().lower() for item in values if item.strip()}

    def source_matches(source: SourceConfig, selectors: set[str]) -> bool:
        return source.id.lower() in selectors or str(source.index) in selectors

    enabled_sources = [item for item in all_sources if item.enabled]
    requested_set = to_selector_set(requested_sources)
    excluded_set = to_selector_set(excluded_sources)

    if requested_set:
        selected_sources = [
            item for item in enabled_sources if source_matches(item, requested_set)
        ]
    else:
        selected_sources = enabled_sources

    excluded_selected_sources = [
        item for item in selected_sources if source_matches(item, excluded_set)
    ]
    if excluded_selected_sources:
        excluded_labels = ", ".join(
            f"{item.index}:{item.id}" for item in excluded_selected_sources
        )
        LOGGER.warning("Skipping excluded sources: %s", excluded_labels)

    return [item for item in selected_sources if not source_matches(item, excluded_set)]


def fetch_job_offers(
    request: JobOffersRequest, session: requests.Session
) -> tuple[list[dict[str, Any]], list[str], list[str]]:
    sources = load_sources(request.config_path)
    selected_sources = select_sources(
        sources,
        request.sources,
        request.excluded_sources,
    )

    if not selected_sources:
        enabled_sources = [item for item in sources if item.enabled]
        if enabled_sources and request.excluded_sources:
            raise RuntimeError(
                "All selected enabled sources are excluded. "
                "Adjust --exclude-sources (or --sources) and try again."
            )

        raise RuntimeError(
            "No enabled source selected. Check --sources value and input/job_sources.json."
        )

    locations = resolve_locations(
        request.location, list(request.locations), request.locations_file
    )
    offers: list[dict[str, Any]] = []
    used_sources: list[str] = []

    for source in selected_sources:
        source_offers = fetch_source_offers(source, request, session, locations)
        offers.extend(source_offers)
        used_sources.append(source.id)

    return offers, used_sources, locations


def build_job_offers_payload(request: JobOffersRequest) -> dict[str, Any]:
    with requests.Session() as session:
        offers, used_sources, locations = fetch_job_offers(request, session)

    return {
        "metadata": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "sources": used_sources,
            "keywords": request.keywords,
            "location": request.location or ", ".join(locations),
            "locations": locations,
            "locations_file": request.locations_file,
            "total_offers": len(offers),
        },
        "offers": offers,
    }
