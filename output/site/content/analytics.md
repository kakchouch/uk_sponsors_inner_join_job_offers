+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-08-31T09:47:03.922789+00:00"
last_research_at = "2026-08-31T09:47:03.922789+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-08-31T09:47:03.922789+00:00
Generated at: 2026-08-31T09:47:03.922789+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 271
- Unique matched jobs: 181
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 418
- Unique matched jobs: 181
- High-confidence unique jobs: 95
- Weighted matched jobs: 128.07
- Weighted high-confidence jobs: 94.92
- Weighted match rate: 30.64%
- Weighted high-confidence rate: 22.71%

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
| London | 46.75 | 65 |
| Manchester | 9.05 | 10 |
| Belfast, Northern Ireland | 4.70 | 6 |
| Bristol | 4.00 | 4 |
| Charing Cross, Central London | 3.00 | 3 |
| Glasgow, Scotland | 3.00 | 3 |
| St. James, Bristol | 3.00 | 3 |
| London, UK | 2.90 | 5 |
| Liverpool | 2.85 | 4 |
| Glasgow | 2.70 | 4 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Ambition Europe Limited | 14.00 | 14 |
| Uber eats | 8.00 | 8 |
| Adecco | 6.00 | 6 |
| Hackajob Ltd | 4.00 | 4 |
| Graphcore | 3.00 | 3 |
| Outpost Technologies | 3.00 | 3 |
| Witherslack Group | 3.00 | 3 |
| BAE Systems | 2.00 | 2 |
| Cytix | 2.00 | 2 |
| Ripple | 2.00 | 2 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Other | 24.50 | 35 |
| Operations / Project Management | 22.60 | 30 |
| Finance / Accounting | 21.40 | 26 |
| Software Engineering | 10.40 | 14 |
| Data / AI | 8.02 | 12 |
| Transport | 4.40 | 7 |
| Cybersecurity / InfoSec | 4.05 | 6 |
| DevOps / Cloud | 4.00 | 4 |
| Sales | 3.20 | 5 |
| Administration / Office | 3.20 | 4 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 91.55 | 138 |
| Global Business Mobility: Senior or Specialist Worker | 30.62 | 34 |
| Global Business Mobility: Graduate Trainee | 2.50 | 3 |
| Creative Worker | 2.40 | 5 |
| Religious Worker | 1.00 | 1 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Leadership | 55.17 | 70 |
| Standard | 54.15 | 83 |
| Senior | 16.25 | 25 |
| Entry | 2.50 | 3 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 94.00 | 94 |
| 0.50 recruiter_or_ambiguous | 19.00 | 38 |
| 0.20 substring_only | 8.20 | 41 |
| 0.85 fuzzy_strong | 5.95 | 7 |
| 0.92 alias_table | 0.92 | 1 |
