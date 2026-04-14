+++
title = "Project Overview"
+++

This project helps non-British jobseekers narrow their UK search to employers that are registered licensed sponsors.

It does this by combining three lightweight steps:

1. Fetch public UK job offers from configured sources.
2. Fetch the latest GOV.UK licensed sponsors register.
3. Match employer names and publish a sponsor-focused list.

## Why this exists

Searching from abroad can be noisy and time-consuming. This site highlights a smaller list of roles where the employer appears in the official sponsor register, so applicants can prioritize faster.

The published report currently focuses on the city list defined in focus_locations.json: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, and Belfast.

## Data and refresh model

- The pipeline generates a Markdown report at sponsored_jobs_report.md.
- The workflow syncs that report into site/content/report.md.
- The scheduled refresh reads its city scope from focus_locations.json.
- The report page renders that Markdown content directly.

## Main scripts

- fetch_job_offers.py: Collects and normalizes job listings.
- fetch_registered_sponsors.py: Pulls and normalizes licensed sponsors data.
- generate_sponsored_jobs_report.py: Runs both fetchers, matches records, and writes report artifacts.

Go to Latest Sponsored Jobs in the menu to view the most recent match list.
