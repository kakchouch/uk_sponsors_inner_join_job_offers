+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-07-30T04:20:19.395071+00:00"
last_research_at = "2026-07-30T04:20:19.395071+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-07-30T04:20:19.395071+00:00
Generated at: 2026-07-30T04:20:19.395071+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 102
- Unique matched jobs: 66
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 321
- Unique matched jobs: 66
- High-confidence unique jobs: 29
- Weighted matched jobs: 44.70
- Weighted high-confidence jobs: 29.00
- Weighted match rate: 13.93%
- Weighted high-confidence rate: 9.03%

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
| London | 14.95 | 24 |
| Glasgow | 4.00 | 4 |
| London, UK | 2.85 | 4 |
| Stockland Bristol, Bridgwater | 2.00 | 2 |
| Belfast, Northern Ireland | 1.90 | 5 |
| Southampton | 1.70 | 3 |
| East London | 1.50 | 2 |
| Manchester, Greater Manchester | 1.50 | 2 |
| Leeds | 1.20 | 2 |
| Altrincham, Greater Manchester | 1.00 | 1 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Uber eats | 6.00 | 6 |
| eFinancialCareers | 4.00 | 4 |
| DX Network Services | 3.00 | 3 |
| Robert Half | 3.00 | 3 |
| Sphere Digital Recruitment | 2.00 | 2 |
| Teleperformance Ltd | 2.00 | 2 |
| Davies Group | 1.00 | 1 |
| Handle Recruitment | 1.00 | 1 |
| Otis | 1.00 | 1 |
| Robert Walters | 1.00 | 1 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Other | 10.55 | 12 |
| Finance / Accounting | 6.70 | 9 |
| Operations / Project Management | 5.40 | 8 |
| Data / AI | 4.75 | 8 |
| Logistics / Supply Chain | 3.00 | 3 |
| Cybersecurity / InfoSec | 2.70 | 4 |
| Administration / Office | 2.40 | 5 |
| Software Engineering | 2.20 | 5 |
| Customer Support / Success | 2.00 | 2 |
| Transport | 1.00 | 2 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 24.50 | 38 |
| Global Business Mobility: Senior or Specialist Worker | 18.00 | 24 |
| Creative Worker | 2.00 | 3 |
| Charity Worker | 0.20 | 1 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 28.45 | 40 |
| Leadership | 14.15 | 21 |
| Senior | 2.10 | 5 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 29.00 | 29 |
| 0.50 recruiter_or_ambiguous | 9.50 | 19 |
| 0.85 fuzzy_strong | 3.40 | 4 |
| 0.20 substring_only | 2.80 | 14 |
| 0.92 alias_table | 0.00 | 0 |
