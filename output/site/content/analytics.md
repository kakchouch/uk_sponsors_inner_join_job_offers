+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-11-16T11:19:16.516446+00:00"
last_research_at = "2026-11-16T11:19:16.516446+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-11-16T11:19:16.516446+00:00
Generated at: 2026-11-16T11:19:16.516446+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 666
- Unique matched jobs: 436
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 848
- Unique matched jobs: 436
- High-confidence unique jobs: 199
- Weighted matched jobs: 286.85
- Weighted high-confidence jobs: 199.00
- Weighted match rate: 33.83%
- Weighted high-confidence rate: 23.47%

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
| London | 144.45 | 250 |
| London, UK | 19.45 | 23 |
| London, England, United Kingdom | 16.00 | 22 |
| UK - London | 10.00 | 10 |
| Manchester | 7.65 | 12 |
| London (hybrid) | 5.00 | 5 |
| Leeds | 4.50 | 5 |
| London Office | 4.20 | 5 |
| Brighton | 3.40 | 5 |
| Bristol, UK | 3.00 | 3 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Airwallex | 11.00 | 11 |
| Hived | 10.00 | 10 |
| Acturis | 8.00 | 8 |
| Uber eats | 8.00 | 8 |
| Sensor Tower | 7.00 | 7 |
| iwoca | 7.00 | 7 |
| Carwow | 6.00 | 6 |
| Openai | 6.00 | 6 |
| Witherslack Group | 5.00 | 5 |
| hyperexponential | 5.00 | 5 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Operations / Project Management | 73.90 | 104 |
| Other | 67.10 | 89 |
| Data / AI | 22.70 | 43 |
| Software Engineering | 17.70 | 27 |
| Administration / Office | 12.20 | 19 |
| Sales | 11.50 | 21 |
| Finance / Accounting | 11.15 | 17 |
| Cybersecurity / InfoSec | 9.40 | 18 |
| HR / Recruitment | 6.75 | 11 |
| Legal | 5.90 | 9 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 211.65 | 342 |
| Global Business Mobility: Senior or Specialist Worker | 67.50 | 85 |
| Scale-up | 5.00 | 5 |
| Global Business Mobility: Graduate Trainee | 2.00 | 2 |
| Creative Worker | 0.50 | 1 |
| Charity Worker | 0.20 | 1 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 120.45 | 187 |
| Leadership | 114.10 | 170 |
| Senior | 44.60 | 69 |
| Entry | 7.70 | 10 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 199.00 | 199 |
| 0.50 recruiter_or_ambiguous | 62.00 | 124 |
| 0.20 substring_only | 21.60 | 108 |
| 0.85 fuzzy_strong | 4.25 | 5 |
| 0.92 alias_table | 0.00 | 0 |
