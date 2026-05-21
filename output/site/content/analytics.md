+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-05-21T07:02:54.601098+00:00"
last_research_at = "2026-05-21T07:02:54.601098+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-05-21T07:02:54.601098+00:00
Generated at: 2026-05-21T07:02:54.601098+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 244
- Unique matched jobs: 122
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 276
- Unique matched jobs: 122
- High-confidence unique jobs: 93
- Weighted matched jobs: 102.70
- Weighted high-confidence jobs: 93.00
- Weighted match rate: 37.21%
- Weighted high-confidence rate: 33.70%

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
| London, UK | 17.70 | 19 |
| London | 10.20 | 16 |
| Belfast, Northern Ireland | 8.70 | 10 |
| Glasgow, Scotland | 7.00 | 7 |
| Leeds | 6.70 | 8 |
| Manchester | 6.20 | 7 |
| Bristol | 5.50 | 6 |
| Glasgow | 5.00 | 5 |
| Bristol, South West England | 3.20 | 4 |
| Langbank, Port Glasgow | 3.00 | 3 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Hays | 42.00 | 42 |
| Sky | 19.00 | 19 |
| eFinancialCareers | 8.00 | 8 |
| BAE Systems | 6.00 | 6 |
| BDO UK | 3.00 | 3 |
| Kier Group | 3.00 | 3 |
| Teleperformance | 3.00 | 3 |
| HAYS | 2.00 | 2 |
| Witherslack Group | 2.00 | 2 |
| DX Network Services | 1.00 | 1 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Finance / Accounting | 34.70 | 37 |
| Other | 19.40 | 22 |
| Operations / Project Management | 11.30 | 16 |
| Data / AI | 7.70 | 9 |
| Banking / Financial Services | 4.00 | 4 |
| Logistics / Supply Chain | 4.00 | 4 |
| Cybersecurity / InfoSec | 3.40 | 5 |
| Insurance | 3.00 | 3 |
| Administration / Office | 2.40 | 4 |
| Construction | 2.00 | 2 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Global Business Mobility: Senior or Specialist Worker | 76.50 | 77 |
| Skilled Worker | 25.70 | 44 |
| Creative Worker | 0.50 | 1 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 61.20 | 71 |
| Leadership | 29.70 | 36 |
| Senior | 11.60 | 14 |
| Entry | 0.20 | 1 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 93.00 | 93 |
| 0.50 recruiter_or_ambiguous | 6.50 | 13 |
| 0.20 substring_only | 3.20 | 16 |
| 0.85 fuzzy_strong | 0.00 | 0 |
| 0.92 alias_table | 0.00 | 0 |
