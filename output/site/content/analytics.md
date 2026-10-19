+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-10-19T08:54:33.831104+00:00"
last_research_at = "2026-10-19T08:54:33.831104+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-10-19T08:54:33.831104+00:00
Generated at: 2026-10-19T08:54:33.831104+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 682
- Unique matched jobs: 421
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 808
- Unique matched jobs: 421
- High-confidence unique jobs: 207
- Weighted matched jobs: 292.20
- Weighted high-confidence jobs: 207.00
- Weighted match rate: 36.16%
- Weighted high-confidence rate: 25.62%

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
| London | 168.95 | 245 |
| London, UK | 29.60 | 33 |
| London, England, United Kingdom | 10.70 | 20 |
| Belfast, Northern Ireland | 7.60 | 11 |
| Bristol | 6.50 | 7 |
| London, England | 5.60 | 8 |
| Stratford, East London | 4.00 | 4 |
| East London | 3.20 | 4 |
| Manchester | 3.00 | 3 |
| London Office | 2.70 | 4 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Openai | 18.00 | 18 |
| Perk | 17.00 | 17 |
| Carwow | 16.00 | 16 |
| Honest Burgers | 11.00 | 11 |
| Uber eats | 10.00 | 10 |
| Synthesia | 8.00 | 8 |
| Anaplan | 7.00 | 7 |
| Sanity | 7.00 | 7 |
| databricks | 5.00 | 5 |
| Adecco | 4.00 | 4 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Operations / Project Management | 65.35 | 88 |
| Other | 59.35 | 80 |
| Data / AI | 34.10 | 49 |
| Software Engineering | 27.80 | 44 |
| Sales | 25.20 | 39 |
| Administration / Office | 16.90 | 24 |
| DevOps / Cloud | 8.85 | 12 |
| Finance / Accounting | 8.50 | 12 |
| Cybersecurity / InfoSec | 7.30 | 12 |
| Operations | 6.40 | 8 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 167.20 | 263 |
| Global Business Mobility: Senior or Specialist Worker | 117.50 | 148 |
| Global Business Mobility: Graduate Trainee | 4.00 | 4 |
| Creative Worker | 2.00 | 4 |
| Scale-up | 1.00 | 1 |
| Government Authorised Exchange | 0.50 | 1 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 127.60 | 195 |
| Leadership | 110.65 | 149 |
| Senior | 49.15 | 68 |
| Entry | 4.80 | 9 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 207.00 | 207 |
| 0.50 recruiter_or_ambiguous | 55.50 | 111 |
| 0.20 substring_only | 17.80 | 89 |
| 0.85 fuzzy_strong | 11.90 | 14 |
| 0.92 alias_table | 0.00 | 0 |
