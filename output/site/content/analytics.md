+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-04-27T06:11:45.959033+00:00"
last_research_at = "2026-04-27T06:11:45.959033+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-04-27T06:11:45.959033+00:00
Generated at: 2026-04-27T06:11:45.959033+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 190
- Unique matched jobs: 119
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 255
- Unique matched jobs: 119
- High-confidence unique jobs: 72
- Weighted matched jobs: 91.85
- Weighted high-confidence jobs: 72.00
- Weighted match rate: 36.02%
- Weighted high-confidence rate: 28.24%

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
| London | 20.05 | 36 |
| London, UK | 16.35 | 17 |
| Belfast, Northern Ireland | 7.00 | 7 |
| Manchester, Greater Manchester | 6.00 | 6 |
| Glasgow, Scotland | 5.00 | 5 |
| Liverpool, Merseyside | 5.00 | 5 |
| Bristol, South West England | 4.00 | 4 |
| Bristol | 3.50 | 4 |
| Leeds | 2.00 | 3 |
| The City, Central London | 2.00 | 2 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Hays | 32.00 | 32 |
| HAYS | 14.00 | 14 |
| Ambition Europe Limited | 6.00 | 6 |
| NG Bailey | 4.00 | 4 |
| eFinancialCareers | 4.00 | 4 |
| Network Plus | 2.00 | 2 |
| Tradewind Recruitment | 2.00 | 2 |
| Birketts LLP | 1.00 | 1 |
| Circle Group | 1.00 | 1 |
| Gail's | 1.00 | 1 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Finance / Accounting | 31.20 | 32 |
| Other | 24.15 | 33 |
| Operations / Project Management | 9.55 | 15 |
| Administration / Office | 5.00 | 6 |
| Data / AI | 3.70 | 5 |
| Skilled Trades | 2.20 | 4 |
| Legal | 2.20 | 3 |
| Sales | 2.00 | 2 |
| Cybersecurity / InfoSec | 1.70 | 3 |
| HR / Recruitment | 1.50 | 2 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Global Business Mobility: Senior or Specialist Worker | 54.50 | 62 |
| Skilled Worker | 37.15 | 56 |
| Seasonal Worker | 0.20 | 1 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 59.30 | 81 |
| Leadership | 23.35 | 28 |
| Senior | 9.20 | 10 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 72.00 | 72 |
| 0.50 recruiter_or_ambiguous | 12.00 | 24 |
| 0.85 fuzzy_strong | 4.25 | 5 |
| 0.20 substring_only | 3.60 | 18 |
| 0.92 alias_table | 0.00 | 0 |
