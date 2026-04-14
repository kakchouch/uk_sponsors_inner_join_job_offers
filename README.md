# uk_sponsors_inner_join_job_offers
A simple script matching publicly available job offers with UK Gov registered sponsors.

## Project Goal

The goal of this project is to help non-British jobseekers quickly identify UK job offers that are more likely to support visa sponsorship, by matching publicly available job listings with the UK Government register of licensed sponsors.

## Target Audience

- Non-British jobseekers looking for UK roles with sponsorship potential
- Beginner developers who want a simple and transparent script they can run and adapt
- Community maintainers who want to publish updated sponsorship-matched job lists

## Use Cases

- Filter a large set of UK job postings to prioritize employers on the licensed sponsor register
- Reduce manual research time before applying to jobs from abroad
- Generate recurring sponsor-matched job lists for a lightweight static website
- Support a GitHub workflow that refreshes and republishes matching results regularly

## Development Model

This project is developed with AI assistance and reviewed by the maintainer before changes are accepted.

For contribution rules and review expectations, see CONTRIBUTING.md.

## Script: Job Offers Fetcher

The first script in this repository fetches job offers from public job APIs.
Source databases are configured in JSON for easy extension.

Current API sources:
- Adzuna
- Reed

### Files

- [fetch_job_offers.py](fetch_job_offers.py): Main Python script that reads source definitions, calls APIs, and exports a normalized JSON file.
- [job_sources.json](job_sources.json): Source registry and per-source defaults.
- [.env.example](.env.example): Required API credential variable names.
- [requirements.txt](requirements.txt): Python dependencies.

### Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set credentials as environment variables:

```bash
export ADZUNA_APP_ID="your_adzuna_app_id"
export ADZUNA_APP_KEY="your_adzuna_app_key"
export REED_API_KEY="your_reed_api_key"
```

Windows PowerShell equivalent:

```powershell
$env:ADZUNA_APP_ID="your_adzuna_app_id"
$env:ADZUNA_APP_KEY="your_adzuna_app_key"
$env:REED_API_KEY="your_reed_api_key"
```

### Run

```bash
python fetch_job_offers.py --keywords "data analyst" --location "London" --results-per-page 30
```

Useful options:
- `--sources adzuna reed`: Select specific sources from [job_sources.json](job_sources.json).
- `--config path/to/custom_sources.json`: Use an alternative source registry.
- `--output path/to/job_offers.json`: Write output to a custom file.

The script exports a normalized JSON file (`job_offers.json` by default) containing:
- `metadata`: run context (time, sources, query, count)
- `offers`: unified job objects from all selected sources

## Script: Registered Sponsors Fetcher

This script fetches the latest Worker and Temporary Worker licensed sponsors CSV from GOV.UK,
normalizes its column names, and exports a JSON file.

### File

- [fetch_registered_sponsors.py](fetch_registered_sponsors.py): Fetches the GOV.UK sponsors register and exports normalized JSON.

### Run

```bash
python fetch_registered_sponsors.py
```

Useful options:
- `--page-url https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers`: Use a custom publication page URL.
- `--output path/to/registered_sponsors.json`: Write output to a custom path.
- `--timeout 30`: Set request timeout in seconds.

The script exports a JSON file (`registered_sponsors.json` by default) containing:
- `metadata`: run context (generation time, publication URL, CSV URL, original headers, count)
- `sponsors`: normalized sponsor records from the latest GOV.UK CSV
