+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-05-28T07:04:14.084584+00:00"
last_research_at = "2026-05-28T07:04:14.084584+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-05-28T07:04:14.084584+00:00
Generated at: 2026-05-28T07:04:14.084584+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 198
- Unique matched jobs: 116
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 282
- Unique matched jobs: 116
- High-confidence unique jobs: 78
- Weighted matched jobs: 92.45
- Weighted high-confidence jobs: 78.00
- Weighted match rate: 32.78%
- Weighted high-confidence rate: 27.66%

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
| London, UK | 13.00 | 14 |
| Manchester | 7.95 | 10 |
| London | 7.20 | 17 |
| Belfast, Northern Ireland | 7.00 | 7 |
| Glasgow, Scotland | 6.00 | 6 |
| Manchester, Greater Manchester | 5.00 | 5 |
| The City, Central London | 5.00 | 5 |
| Bristol | 4.85 | 6 |
| Bristol, South West England | 3.50 | 4 |
| South East London, London | 2.85 | 3 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Hays | 45.00 | 45 |
| Tradewind Recruitment | 8.00 | 8 |
| Aspire People Limited | 5.00 | 5 |
| BAE Systems | 4.00 | 4 |
| Adecco | 1.00 | 1 |
| BDO | 1.00 | 1 |
| Edina | 1.00 | 1 |
| HAYS | 1.00 | 1 |
| Leeds Building Society | 1.00 | 1 |
| Manpower | 1.00 | 1 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Finance / Accounting | 27.70 | 30 |
| Operations / Project Management | 13.70 | 19 |
| Other | 10.90 | 13 |
| Education / Teaching | 8.80 | 12 |
| Data / AI | 6.40 | 9 |
| Administration / Office | 6.30 | 9 |
| Cybersecurity / InfoSec | 4.00 | 4 |
| Creative / Media | 2.20 | 3 |
| Software Engineering | 2.00 | 3 |
| Banking / Financial Services | 2.00 | 2 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Global Business Mobility: Senior or Specialist Worker | 57.00 | 59 |
| Skilled Worker | 35.45 | 57 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 44.45 | 57 |
| Leadership | 31.40 | 40 |
| Senior | 13.40 | 15 |
| Entry | 3.20 | 4 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 78.00 | 78 |
| 0.50 recruiter_or_ambiguous | 6.00 | 12 |
| 0.85 fuzzy_strong | 4.25 | 5 |
| 0.20 substring_only | 4.20 | 21 |
| 0.92 alias_table | 0.00 | 0 |
