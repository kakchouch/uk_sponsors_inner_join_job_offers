+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-05-04T06:23:34.867639+00:00"
last_research_at = "2026-05-04T06:23:34.867639+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-05-04T06:23:34.867639+00:00
Generated at: 2026-05-04T06:23:34.867639+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 173
- Unique matched jobs: 104
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 367
- Unique matched jobs: 104
- High-confidence unique jobs: 71
- Weighted matched jobs: 83.15
- Weighted high-confidence jobs: 71.00
- Weighted match rate: 22.66%
- Weighted high-confidence rate: 19.35%

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
| London, UK | 26.40 | 29 |
| London | 7.40 | 9 |
| Glasgow, Scotland | 7.00 | 7 |
| Belfast, Northern Ireland | 5.00 | 5 |
| Bristol, South West England | 4.05 | 5 |
| Manchester, Greater Manchester | 4.00 | 4 |
| Liverpool, Merseyside | 3.20 | 4 |
| The City, Central London | 2.00 | 2 |
| South East London, London | 1.20 | 3 |
| East London | 1.20 | 2 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Hays | 40.00 | 40 |
| Ambition Europe Limited | 3.00 | 3 |
| HAYS | 3.00 | 3 |
| Etihad Airways | 2.00 | 2 |
| Evri | 2.00 | 2 |
| NG Bailey | 2.00 | 2 |
| Teleperformance | 2.00 | 2 |
| eFinancialCareers | 2.00 | 2 |
| AKT II | 1.00 | 1 |
| Adecco | 1.00 | 1 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Finance / Accounting | 27.00 | 28 |
| Operations / Project Management | 13.40 | 16 |
| Other | 9.10 | 16 |
| Data / AI | 8.10 | 12 |
| Banking / Financial Services | 5.00 | 5 |
| Construction | 4.00 | 4 |
| Transport | 2.50 | 3 |
| Sales | 2.05 | 3 |
| Cybersecurity / InfoSec | 1.50 | 2 |
| Education / Teaching | 1.45 | 4 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Global Business Mobility: Senior or Specialist Worker | 55.50 | 59 |
| Skilled Worker | 26.65 | 44 |
| Global Business Mobility: Graduate Trainee | 1.00 | 1 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 44.35 | 61 |
| Leadership | 26.40 | 29 |
| Senior | 11.20 | 12 |
| Entry | 1.20 | 2 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 71.00 | 71 |
| 0.50 recruiter_or_ambiguous | 6.00 | 12 |
| 0.20 substring_only | 3.60 | 18 |
| 0.85 fuzzy_strong | 2.55 | 3 |
| 0.92 alias_table | 0.00 | 0 |
