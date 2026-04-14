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

## Data and refresh model

- The pipeline writes the latest match output to matched_sponsored_jobs.json.
- This Hugo site reads that file at build time.
- The report page therefore reflects the latest generated list in the repository.

## Main scripts

- fetch_job_offers.py: Collects and normalizes job listings.
- fetch_registered_sponsors.py: Pulls and normalizes licensed sponsors data.
- generate_sponsored_jobs_report.py: Runs both fetchers, matches records, and writes report artifacts.

Go to Latest Sponsored Jobs in the menu to view the most recent match list.
