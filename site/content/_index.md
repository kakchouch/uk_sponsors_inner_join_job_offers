+++
title = "Project Overview"
+++

This project helps non-British jobseekers narrow their UK search to employers that are registered licensed sponsors.

Repository: [uk_sponsors_inner_join_job_offers](https://github.com/kakchouch/uk_sponsors_inner_join_job_offers)

It does this by combining three lightweight steps:

1. Fetch public UK job offers from configured sources.
2. Fetch the latest GOV.UK licensed sponsors register.
3. Match employer names and publish a sponsor-focused list.

## Why this exists

Searching from abroad can be noisy and time-consuming. This site highlights a smaller list of roles where the employer appears in the official sponsor register, so applicants can prioritize faster.

The published report currently focuses on the city list defined in input/focus_locations.json: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, and Belfast.

## Data and refresh model

- The pipeline generates a Markdown report at output/reports/sponsored_jobs_report.md.
- The analytics step generates a Markdown report at output/reports/market_analytics_report.md.
- The workflow commits generated Hugo-ready content from output/site/content/report.md.
- The analytics workflow commits generated Hugo-ready content from output/site/content/analytics.md.
- The scheduled refresh reads its city scope from input/focus_locations.json.
- The report and analytics pages render generated Markdown content directly.

### Quality-Score Weighting in Analytics

All analytics metrics are computed using **quality-score weighting**. This means:
- Each job's contribution to market totals is proportional to its match confidence
- Exact matches (1.00 score) contribute fully; lower-confidence matches (0.20-0.92) contribute proportionally
- Result: more accurate representation of sponsorship opportunities, with higher-confidence matches having greater influence

Visit the [Market Analytics](/analytics/) page to see weighted job distributions by location, employer, title, visa route, and seniority.

## Main scripts

- fetch_job_offers.py: Collects and normalizes job listings.
- fetch_registered_sponsors.py: Pulls and normalizes licensed sponsors data.
- generate_sponsored_jobs_report.py: Runs both fetchers, matches records, and writes report artifacts.

Go to Latest Sponsored Jobs in the menu to view the most recent match list.

Go to Market Analytics in the menu to view the latest deduplicated summary charts and employer/location breakdowns.
