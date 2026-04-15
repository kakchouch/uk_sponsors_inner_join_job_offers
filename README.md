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
- Arbeitnow

### Files

- [fetch_job_offers.py](fetch_job_offers.py): Main Python script that reads source definitions, calls APIs, and exports a normalized JSON file.
- [input/focus_locations.json](input/focus_locations.json): Shared curated city list used by the scheduled report refresh.
- [input/job_sources.json](input/job_sources.json): Source registry and per-source defaults.
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
python fetch_job_offers.py --keywords "data analyst" --locations-file input/focus_locations.json --results-per-page 30
```

To scan the whole configured sites without keyword/location filtering:

```bash
python fetch_job_offers.py --results-per-page 100
```

Useful options:
- `--sources adzuna reed arbeitnow` or `--sources 1 2 3`: Select specific sources by id or by 1-based index from [input/job_sources.json](input/job_sources.json) order.
- `--exclude-sources reed` or `--exclude-sources 2`: Exclude one or more sources by id or index.
- `--sources adzuna reed arbeitnow --exclude-sources reed`: Include then exclude (exclusion is applied last).
- `--locations-file input/focus_locations.json`: Load the city list from a JSON file containing a `locations` array.
- `--locations London Glasgow Manchester`: Query several cities separately and merge the results.
- `--config path/to/custom_sources.json`: Use an alternative source registry.
- `--output path/to/job_offers.json`: Write output to a custom file. The default is `output/raw/job_offers.json`.
- `--single-page`: Fetch only one page per source (legacy behavior).
- `--max-pages 10`: Limit fetched pages per source when full pagination is enabled.

Source index mapping is derived from the source order in [input/job_sources.json](input/job_sources.json). With the current default file:
- `1`: `adzuna`
- `2`: `reed`
- `3`: `arbeitnow`

If a source is excluded, it is skipped before authentication checks. This means missing API credentials for excluded sources do not raise an error, and only a skip log message is emitted.

If a selected source fails before returning any results, that source is skipped. If it fails only after some pages were already collected or hits an API cap mid-pagination, the partial results are kept and the source is marked as incomplete in metadata.

If all enabled selected sources are excluded, the fetch pipeline stops early with a clear error instead of running with an empty source set.

The script exports a normalized JSON file (`output/raw/job_offers.json` by default) containing:
- `metadata`: run context (time, sources, query, count)
- `offers`: unified job objects from all selected sources

By default, the script now paginates through all available result pages for each selected source.
By default, no keyword or location filter is applied, so it fetches all available job types.
The scheduled site publication narrows the search using [input/focus_locations.json](input/focus_locations.json), which currently contains London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, and Belfast.

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
- `--output path/to/registered_sponsors.json`: Write output to a custom path. The default is `output/raw/registered_sponsors.json`.
- `--timeout 30`: Set request timeout in seconds.

The script exports a JSON file (`output/raw/registered_sponsors.json` by default) containing:
- `metadata`: run context (generation time, publication URL, CSV URL, original headers, count)
- `sponsors`: normalized sponsor records from the latest GOV.UK CSV

## Script: Sponsor-Matched Markdown Report

This script runs both fetchers, matches job offer companies against registered sponsor names,
and exports a Markdown report.

The matcher now assigns a confidence score to each output row using this scale:
- `1.00`: exact normalized sponsor name match
- `0.92`: alias table match from `input/alias_table.json`
- `0.85`: strong fuzzy match
- `0.50`: recruiter or ambiguous best-candidate match using `input/headhunters.json`
- `0.20`: substring-only match

### General Caveat
Output job offers do not guarantee the company sponsors for those specific positions.

### File

- [generate_sponsored_jobs_report.py](generate_sponsored_jobs_report.py): Runs both fetch scripts, performs matching, and writes a Markdown summary table.

### Run

```bash
python generate_sponsored_jobs_report.py --keywords "software engineer" --locations-file input/focus_locations.json
```

To fetch all available job types before matching:

```bash
python generate_sponsored_jobs_report.py
```

Useful options:
- `--sources adzuna reed arbeitnow` or `--sources 1 2 3`: Select specific job sources by id or by 1-based index from [input/job_sources.json](input/job_sources.json) order.
- `--exclude-sources reed` or `--exclude-sources 2`: Exclude one or more job sources by id or index.
- `--locations-file input/focus_locations.json`: Load the city list from a JSON file containing a `locations` array.
- `--locations London Glasgow Manchester`: Query several cities separately and merge the results before matching.
- `--jobs-output output/raw/job_offers.json`: Path for fetched offers JSON.
- `--sponsors-output output/raw/registered_sponsors.json`: Path for fetched sponsors JSON.
- `--markdown-output output/reports/sponsored_jobs_report.md`: Path for Markdown output file.
- `--matched-json-output output/reports/matched_sponsored_jobs.json`: Path for JSON output containing only matched records.
- `--site-report-output output/site/content/report.md`: Path for Hugo-ready generated content.

The script outputs:
- fetched offers JSON (default: `output/raw/job_offers.json`)
- fetched sponsors JSON (default: `output/raw/registered_sponsors.json`)
- Markdown report (default: `output/reports/sponsored_jobs_report.md`)
- matched records JSON (default: `output/reports/matched_sponsored_jobs.json`)
- Hugo content page (default: `output/site/content/report.md`)

Matched rows now include `quality_score`, `match_score`, and `match_type` metadata in the JSON export, and the Markdown table includes a `Quality Score` column for review.

If a job source hits an API cap or its collection fails after retries, the report still completes. Fully failed sources are recorded as skipped, while partial sources remain in the dataset and are recorded as incomplete in the generated metadata and Markdown summary.

## Output Layout

All generated artifacts now live under the dedicated [output](output) directory:

- `output/raw/`: transient fetch payloads for job offers and sponsors
- `output/reports/`: tracked Markdown and matched-record exports
- `output/site/content/`: tracked Hugo-ready generated content mounted into the site build

The Hugo site reads the generated report from `output/site/content/report.md`, so the report publishing flow no longer writes generated content into the hand-maintained `site/content/` tree.

