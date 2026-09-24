+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-09-24T08:28:53.000476+00:00"
last_research_at = "2026-09-24T08:28:53.000476+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-09-24T08:28:53.000476+00:00
Generated at: 2026-09-24T08:28:53.000476+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 288
- Unique matched jobs: 175
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 389
- Unique matched jobs: 175
- High-confidence unique jobs: 57
- Weighted matched jobs: 105.30
- Weighted high-confidence jobs: 57.00
- Weighted match rate: 27.07%
- Weighted high-confidence rate: 14.65%

## Charts

All charts below use quality-score-weighted totals rather than raw row counts.

### Top Locations

![Top locations chart](/charts/top_locations.png)

### Top Employers (High Confidence)

![Top employers chart](/charts/top_employers.png)

### Match Quality Distribution

![Match quality chart](/charts/match_quality.png)

### Top Job Title Families

![Top title families chart](/charts/top_titles.png)

### Visa Routes

![Visa routes chart](/charts/routes.png)

### Title Seniority

![Title seniority chart](/charts/seniority.png)

## Top Locations

| Location | Weighted score | Raw jobs |
|---|---|---|
| London | 53.20 | 91 |
| North London | 4.20 | 5 |
| Bristol | 3.50 | 6 |
| East London | 3.20 | 4 |
| West London | 3.00 | 3 |
| Ocean Village, Southampton | 2.90 | 5 |
| Belfast, Northern Ireland | 2.55 | 5 |
| Manchester | 2.10 | 5 |
| Bristol, South West England | 2.00 | 2 |
| London Office | 2.00 | 2 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Tradewind Recruitment | 9.00 | 9 |
| Robert Walters | 5.00 | 5 |
| Adecco | 4.00 | 4 |
| Sphere Digital Recruitment | 4.00 | 4 |
| BAE Systems | 3.00 | 3 |
| Network Plus | 3.00 | 3 |
| Uber eats | 3.00 | 3 |
| Ambition Europe Limited | 2.00 | 2 |
| Robert Half | 2.00 | 2 |
| databricks | 2.00 | 2 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Other | 20.10 | 30 |
| Data / AI | 14.70 | 27 |
| Operations / Project Management | 14.10 | 24 |
| Software Engineering | 11.30 | 23 |
| Finance / Accounting | 10.00 | 14 |
| Legal | 5.85 | 8 |
| Education / Teaching | 4.20 | 5 |
| Cybersecurity / InfoSec | 4.05 | 6 |
| Sales | 3.00 | 4 |
| DevOps / Cloud | 2.50 | 3 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 51.80 | 89 |
| Global Business Mobility: Senior or Specialist Worker | 48.00 | 80 |
| Global Business Mobility: Graduate Trainee | 3.00 | 3 |
| Creative Worker | 1.50 | 2 |
| Charity Worker | 1.00 | 1 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 54.40 | 88 |
| Leadership | 31.60 | 56 |
| Senior | 18.30 | 30 |
| Entry | 1.00 | 1 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 57.00 | 57 |
| 0.50 recruiter_or_ambiguous | 39.00 | 78 |
| 0.20 substring_only | 7.60 | 38 |
| 0.85 fuzzy_strong | 1.70 | 2 |
| 0.92 alias_table | 0.00 | 0 |
