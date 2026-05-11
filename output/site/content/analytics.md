+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-05-11T06:51:28.449421+00:00"
last_research_at = "2026-05-11T06:51:28.449421+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-05-11T06:51:28.449421+00:00
Generated at: 2026-05-11T06:51:28.449421+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 209
- Unique matched jobs: 119
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 303
- Unique matched jobs: 119
- High-confidence unique jobs: 89
- Weighted matched jobs: 102.05
- Weighted high-confidence jobs: 89.00
- Weighted match rate: 33.68%
- Weighted high-confidence rate: 29.37%

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
| London, UK | 20.70 | 21 |
| London | 19.00 | 23 |
| Belfast, Northern Ireland | 12.20 | 13 |
| Manchester, Greater Manchester | 6.20 | 7 |
| Bristol, South West England | 5.00 | 5 |
| Ocean Village, Southampton | 3.20 | 4 |
| Glasgow, Scotland | 3.00 | 3 |
| Liverpool, Merseyside | 3.00 | 3 |
| The City, Central London | 3.00 | 3 |
| Manchester | 2.20 | 3 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Hays | 53.00 | 53 |
| eFinancialCareers | 15.00 | 15 |
| BAE Systems | 5.00 | 5 |
| NG Bailey | 5.00 | 5 |
| Witherslack Group | 3.00 | 3 |
| DX Network Services | 1.00 | 1 |
| DX Network Services Limited | 1.00 | 1 |
| ESS | 1.00 | 1 |
| High Finance  Limited | 1.00 | 1 |
| Jazz Pharmaceuticals | 1.00 | 1 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Finance / Accounting | 29.00 | 29 |
| Operations / Project Management | 20.10 | 23 |
| Other | 17.95 | 24 |
| Banking / Financial Services | 8.00 | 8 |
| Administration / Office | 5.70 | 7 |
| Data / AI | 5.20 | 7 |
| Construction | 2.00 | 2 |
| Insurance | 2.00 | 2 |
| Software Engineering | 2.00 | 2 |
| Transport | 1.50 | 3 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Global Business Mobility: Senior or Specialist Worker | 63.00 | 67 |
| Skilled Worker | 39.05 | 52 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 55.70 | 68 |
| Leadership | 31.30 | 35 |
| Senior | 14.05 | 15 |
| Entry | 1.00 | 1 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 89.00 | 89 |
| 0.50 recruiter_or_ambiguous | 8.50 | 17 |
| 0.85 fuzzy_strong | 2.55 | 3 |
| 0.20 substring_only | 2.00 | 10 |
| 0.92 alias_table | 0.00 | 0 |
