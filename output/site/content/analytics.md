+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-07-20T04:30:09.971953+00:00"
last_research_at = "2026-07-20T04:30:09.971953+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-07-20T04:30:09.971953+00:00
Generated at: 2026-07-20T04:30:09.971953+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 197
- Unique matched jobs: 116
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 310
- Unique matched jobs: 116
- High-confidence unique jobs: 74
- Weighted matched jobs: 90.20
- Weighted high-confidence jobs: 73.60
- Weighted match rate: 29.10%
- Weighted high-confidence rate: 23.74%

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
| London | 26.45 | 31 |
| Manchester | 9.50 | 11 |
| Bristol | 6.35 | 7 |
| Liverpool | 5.70 | 7 |
| Glasgow | 4.70 | 6 |
| Leeds | 4.34 | 5 |
| Belfast, Northern Ireland | 3.50 | 4 |
| Ocean Village, Southampton | 2.50 | 3 |
| Hyde Park, Leeds | 2.00 | 2 |
| South East London, London | 2.00 | 2 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Pearson Plc | 17.00 | 17 |
| eFinancialCareers | 17.00 | 17 |
| Lloyds Banking Group | 3.68 | 4 |
| BAE Systems | 3.00 | 3 |
| Robert Half | 3.00 | 3 |
| Uber eats | 3.00 | 3 |
| Witherslack Group | 3.00 | 3 |
| IQVIA | 2.00 | 2 |
| Robert Walters | 2.00 | 2 |
| Aspire People Limited | 1.00 | 1 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Marketing | 15.20 | 16 |
| Other | 14.40 | 17 |
| Operations / Project Management | 8.37 | 13 |
| Finance / Accounting | 7.70 | 10 |
| Data / AI | 7.44 | 12 |
| Cybersecurity / InfoSec | 6.42 | 7 |
| Administration / Office | 5.70 | 8 |
| Nursing / Care | 4.20 | 5 |
| Software Engineering | 3.42 | 4 |
| Banking / Financial Services | 3.00 | 3 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 46.60 | 67 |
| Global Business Mobility: Senior or Specialist Worker | 36.60 | 39 |
| Creative Worker | 3.50 | 6 |
| Global Business Mobility: Graduate Trainee | 3.50 | 4 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 47.18 | 62 |
| Leadership | 32.62 | 42 |
| Senior | 9.20 | 10 |
| Entry | 1.20 | 2 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 69.00 | 69 |
| 0.50 recruiter_or_ambiguous | 11.50 | 23 |
| 0.92 alias_table | 4.60 | 5 |
| 0.20 substring_only | 3.40 | 17 |
| 0.85 fuzzy_strong | 1.70 | 2 |
