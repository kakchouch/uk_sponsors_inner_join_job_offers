+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-06-11T08:16:59.912355+00:00"
last_research_at = "2026-06-11T08:16:59.912355+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-06-11T08:16:59.912355+00:00
Generated at: 2026-06-11T08:16:59.912355+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 235
- Unique matched jobs: 136
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 289
- Unique matched jobs: 136
- High-confidence unique jobs: 80
- Weighted matched jobs: 101.05
- Weighted high-confidence jobs: 80.00
- Weighted match rate: 34.97%
- Weighted high-confidence rate: 27.68%

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
| London, UK | 23.00 | 23 |
| London | 11.05 | 18 |
| Glasgow, Scotland | 9.50 | 10 |
| Belfast, Northern Ireland | 8.50 | 9 |
| Bristol, South West England | 4.00 | 4 |
| Manchester, Greater Manchester | 4.00 | 4 |
| The City, Central London | 4.00 | 4 |
| Manchester | 3.50 | 10 |
| Bristol | 3.00 | 4 |
| Liverpool, Merseyside | 3.00 | 3 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Hays | 52.00 | 52 |
| BDO UK | 4.00 | 4 |
| Kier Group | 3.00 | 3 |
| Robert Half | 3.00 | 3 |
| Adecco | 2.00 | 2 |
| HAYS | 2.00 | 2 |
| Morgan McKinley | 2.00 | 2 |
| Ramsay Health Care | 2.00 | 2 |
| BAE Systems | 1.00 | 1 |
| Fibrus Networks Ltd | 1.00 | 1 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Finance / Accounting | 37.50 | 39 |
| Operations / Project Management | 13.20 | 15 |
| Other | 11.30 | 21 |
| Data / AI | 6.30 | 11 |
| Legal | 5.20 | 7 |
| Administration / Office | 4.40 | 6 |
| Real Estate / Property | 3.70 | 4 |
| Banking / Financial Services | 3.00 | 3 |
| Education / Teaching | 2.20 | 8 |
| Cybersecurity / InfoSec | 2.00 | 2 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Global Business Mobility: Senior or Specialist Worker | 69.00 | 70 |
| Skilled Worker | 29.55 | 62 |
| Creative Worker | 1.50 | 3 |
| Global Business Mobility: Graduate Trainee | 1.00 | 1 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 53.40 | 78 |
| Leadership | 32.45 | 38 |
| Senior | 13.40 | 15 |
| Entry | 1.80 | 5 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 80.00 | 80 |
| 0.50 recruiter_or_ambiguous | 11.00 | 22 |
| 0.20 substring_only | 5.80 | 29 |
| 0.85 fuzzy_strong | 4.25 | 5 |
| 0.92 alias_table | 0.00 | 0 |
