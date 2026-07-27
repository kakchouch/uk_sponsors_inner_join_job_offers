+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-07-27T04:30:12.904340+00:00"
last_research_at = "2026-07-27T04:30:12.904340+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-07-27T04:30:12.904340+00:00
Generated at: 2026-07-27T04:30:12.904340+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 138
- Unique matched jobs: 86
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 316
- Unique matched jobs: 86
- High-confidence unique jobs: 43
- Weighted matched jobs: 58.81
- Weighted high-confidence jobs: 42.76
- Weighted match rate: 18.61%
- Weighted high-confidence rate: 13.53%

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
| London | 23.95 | 33 |
| Bristol, South West England | 2.00 | 2 |
| Firswood, Manchester | 2.00 | 2 |
| Glasgow | 2.00 | 2 |
| Poplar, East London | 1.84 | 2 |
| City of London | 1.70 | 2 |
| Bristol | 1.50 | 2 |
| Glasgow, Scotland | 1.12 | 2 |
| Chew Stoke, Bristol | 1.00 | 1 |
| Collyhurst, Manchester | 1.00 | 1 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Uber eats | 7.00 | 7 |
| eFinancialCareers | 6.00 | 6 |
| Robert Walters | 4.00 | 4 |
| Robert Half | 3.00 | 3 |
| Barclays | 2.76 | 3 |
| DX Network Services | 2.00 | 2 |
| Network Plus | 2.00 | 2 |
| Sky | 2.00 | 2 |
| Sphere Digital Recruitment | 2.00 | 2 |
| Teleperformance Ltd | 2.00 | 2 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Other | 11.95 | 15 |
| Operations / Project Management | 9.17 | 11 |
| Finance / Accounting | 7.70 | 10 |
| Data / AI | 7.37 | 12 |
| Administration / Office | 5.60 | 8 |
| Cybersecurity / InfoSec | 3.20 | 4 |
| Customer Support / Success | 2.00 | 2 |
| Transport | 1.40 | 4 |
| Software Engineering | 1.20 | 3 |
| Creative / Media | 1.20 | 2 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 33.05 | 56 |
| Global Business Mobility: Senior or Specialist Worker | 20.76 | 23 |
| Creative Worker | 4.00 | 6 |
| Global Business Mobility: Graduate Trainee | 1.00 | 1 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 35.54 | 53 |
| Leadership | 18.92 | 24 |
| Senior | 3.95 | 7 |
| Entry | 0.40 | 2 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 40.00 | 40 |
| 0.50 recruiter_or_ambiguous | 7.00 | 14 |
| 0.20 substring_only | 4.80 | 24 |
| 0.85 fuzzy_strong | 4.25 | 5 |
| 0.92 alias_table | 2.76 | 3 |
