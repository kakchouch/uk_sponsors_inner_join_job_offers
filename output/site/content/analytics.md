+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-07-06T04:47:04.525916+00:00"
last_research_at = "2026-07-06T04:47:04.525916+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-07-06T04:47:04.525916+00:00
Generated at: 2026-07-06T04:47:04.525916+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 194
- Unique matched jobs: 148
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 388
- Unique matched jobs: 148
- High-confidence unique jobs: 107
- Weighted matched jobs: 120.50
- Weighted high-confidence jobs: 107.00
- Weighted match rate: 31.06%
- Weighted high-confidence rate: 27.58%

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
| London | 78.05 | 88 |
| Greater Manchester | 3.00 | 4 |
| South East London | 3.00 | 3 |
| Firswood, Manchester | 2.00 | 2 |
| Hillhead, Glasgow City Centre | 2.00 | 2 |
| Isleworth, West London | 2.00 | 2 |
| Langbank, Port Glasgow | 2.00 | 2 |
| Leeds, West Yorkshire | 1.85 | 2 |
| Manchester | 1.70 | 3 |
| South East London, London | 1.70 | 2 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| eFinancialCareers | 67.00 | 67 |
| Uber eats | 6.00 | 6 |
| Adecco | 3.00 | 3 |
| BAE Systems | 3.00 | 3 |
| Creative Support Ltd | 3.00 | 3 |
| Network Plus | 3.00 | 3 |
| Robert Walters | 3.00 | 3 |
| Tradewind Recruitment | 3.00 | 3 |
| Etihad Airways | 2.00 | 2 |
| Kier Group | 2.00 | 2 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Other | 26.85 | 32 |
| Operations / Project Management | 14.20 | 19 |
| Finance / Accounting | 11.00 | 11 |
| Cybersecurity / InfoSec | 8.00 | 8 |
| Data / AI | 6.95 | 10 |
| Administration / Office | 6.20 | 7 |
| Education / Teaching | 5.80 | 13 |
| Legal | 5.70 | 7 |
| Software Engineering | 5.50 | 6 |
| Banking / Financial Services | 5.00 | 5 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 96.60 | 121 |
| Global Business Mobility: Senior or Specialist Worker | 18.50 | 20 |
| Global Business Mobility: Graduate Trainee | 3.00 | 3 |
| Creative Worker | 2.40 | 4 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 79.10 | 97 |
| Leadership | 34.40 | 40 |
| Senior | 6.40 | 8 |
| Entry | 0.60 | 3 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 107.00 | 107 |
| 0.20 substring_only | 5.60 | 28 |
| 0.50 recruiter_or_ambiguous | 4.50 | 9 |
| 0.85 fuzzy_strong | 3.40 | 4 |
| 0.92 alias_table | 0.00 | 0 |
