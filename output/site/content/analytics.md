+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-06-22T04:57:17.391362+00:00"
last_research_at = "2026-06-22T04:57:17.391362+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-06-22T04:57:17.391362+00:00
Generated at: 2026-06-22T04:57:17.391362+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 230
- Unique matched jobs: 143
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 316
- Unique matched jobs: 143
- High-confidence unique jobs: 104
- Weighted matched jobs: 118.80
- Weighted high-confidence jobs: 104.00
- Weighted match rate: 37.59%
- Weighted high-confidence rate: 32.91%

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
| London | 34.00 | 43 |
| London, UK | 12.85 | 13 |
| Manchester | 9.00 | 10 |
| Belfast, Northern Ireland | 6.90 | 9 |
| Bristol, South West England | 6.00 | 6 |
| Manchester, Greater Manchester | 5.00 | 5 |
| Glasgow, Scotland | 4.50 | 5 |
| Leeds, West Yorkshire | 4.00 | 4 |
| The City, Central London | 4.00 | 4 |
| Glasgow | 3.50 | 4 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Hays | 37.00 | 37 |
| eFinancialCareers | 24.00 | 24 |
| AJ Bell | 8.00 | 8 |
| HAYS | 7.00 | 7 |
| Uber eats | 3.00 | 3 |
| BAE Systems | 2.00 | 2 |
| BDO UK | 2.00 | 2 |
| Davies Group | 2.00 | 2 |
| Etihad Airways | 2.00 | 2 |
| Sphere Digital Recruitment | 2.00 | 2 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Finance / Accounting | 28.20 | 29 |
| Operations / Project Management | 20.70 | 28 |
| Other | 17.45 | 21 |
| Data / AI | 9.90 | 13 |
| Cybersecurity / InfoSec | 7.20 | 8 |
| Administration / Office | 7.00 | 7 |
| Skilled Trades | 3.70 | 6 |
| Banking / Financial Services | 3.00 | 3 |
| Legal | 3.00 | 3 |
| Software Engineering | 3.00 | 3 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 57.80 | 78 |
| Global Business Mobility: Senior or Specialist Worker | 55.50 | 56 |
| Creative Worker | 3.50 | 7 |
| Global Business Mobility: Graduate Trainee | 2.00 | 2 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 68.55 | 83 |
| Leadership | 39.90 | 48 |
| Senior | 9.85 | 11 |
| Entry | 0.50 | 1 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 104.00 | 104 |
| 0.50 recruiter_or_ambiguous | 9.50 | 19 |
| 0.20 substring_only | 3.60 | 18 |
| 0.85 fuzzy_strong | 1.70 | 2 |
| 0.92 alias_table | 0.00 | 0 |
