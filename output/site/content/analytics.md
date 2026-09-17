+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-09-17T08:41:19.695678+00:00"
last_research_at = "2026-09-17T08:41:19.695678+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-09-17T08:41:19.695678+00:00
Generated at: 2026-09-17T08:41:19.695678+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 217
- Unique matched jobs: 152
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 359
- Unique matched jobs: 152
- High-confidence unique jobs: 68
- Weighted matched jobs: 95.50
- Weighted high-confidence jobs: 68.00
- Weighted match rate: 26.60%
- Weighted high-confidence rate: 18.94%

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
| London | 32.80 | 53 |
| Remote, London | 10.00 | 10 |
| London, UK | 4.15 | 12 |
| Portsmouth, Hampshire | 3.00 | 3 |
| Bristol, South West England | 2.50 | 3 |
| Liverpool | 2.00 | 3 |
| Firswood, Manchester | 2.00 | 2 |
| London Hybrid | 2.00 | 2 |
| London, London, United Kingdom | 2.00 | 2 |
| Leeds | 2.00 | 7 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Moniepoint | 12.00 | 12 |
| Uber eats | 10.00 | 10 |
| Clay Labs | 5.00 | 5 |
| BAE Systems | 4.00 | 4 |
| Handle Recruitment | 4.00 | 4 |
| Network Plus | 3.00 | 3 |
| Sphere Digital Recruitment | 3.00 | 3 |
| Adecco | 2.00 | 2 |
| Catapult Sports | 2.00 | 2 |
| Geordie AI | 2.00 | 2 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Other | 22.15 | 32 |
| Operations / Project Management | 19.40 | 27 |
| Administration / Office | 12.60 | 16 |
| Finance / Accounting | 6.80 | 11 |
| Software Engineering | 6.20 | 8 |
| Data / AI | 6.10 | 9 |
| Cybersecurity / InfoSec | 3.30 | 7 |
| Creative / Media | 2.80 | 6 |
| Sales | 2.80 | 6 |
| Skilled Trades | 2.50 | 4 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 63.50 | 115 |
| Global Business Mobility: Senior or Specialist Worker | 26.00 | 29 |
| Global Business Mobility: Graduate Trainee | 4.00 | 4 |
| Creative Worker | 2.00 | 4 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 50.40 | 83 |
| Leadership | 28.75 | 42 |
| Senior | 14.20 | 21 |
| Entry | 2.15 | 6 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 68.00 | 68 |
| 0.50 recruiter_or_ambiguous | 13.50 | 27 |
| 0.20 substring_only | 10.60 | 53 |
| 0.85 fuzzy_strong | 3.40 | 4 |
| 0.92 alias_table | 0.00 | 0 |
