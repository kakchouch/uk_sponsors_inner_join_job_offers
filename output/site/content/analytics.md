+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-10-29T09:59:54.324538+00:00"
last_research_at = "2026-10-29T09:59:54.324538+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-10-29T09:59:54.324538+00:00
Generated at: 2026-10-29T09:59:54.324538+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 1020
- Unique matched jobs: 621
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 1102
- Unique matched jobs: 621
- High-confidence unique jobs: 329
- Weighted matched jobs: 437.10
- Weighted high-confidence jobs: 329.00
- Weighted match rate: 39.66%
- Weighted high-confidence rate: 29.85%

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
| London | 241.95 | 352 |
| Bristol | 34.70 | 45 |
| London, United Kingdom | 28.70 | 34 |
| Manchester | 12.85 | 13 |
| London, UK | 10.25 | 20 |
| Belfast, Northern Ireland | 9.40 | 13 |
| London, England, United Kingdom | 9.20 | 13 |
| London Office | 7.60 | 10 |
| UK - London | 4.00 | 4 |
| UK London, United Kingdom | 4.00 | 4 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Graphcore | 28.00 | 28 |
| Palantir | 27.00 | 27 |
| Spotify | 14.00 | 14 |
| Uber eats | 12.00 | 12 |
| Sparta Commodities | 10.00 | 10 |
| iwoca | 9.00 | 9 |
| Perk | 8.00 | 8 |
| Anaplan | 7.00 | 7 |
| Woven By Toyota | 7.00 | 7 |
| Flock | 6.00 | 6 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Operations / Project Management | 92.30 | 129 |
| Software Engineering | 67.90 | 87 |
| Other | 67.40 | 103 |
| Data / AI | 61.10 | 91 |
| Sales | 31.50 | 44 |
| Administration / Office | 16.35 | 23 |
| Cybersecurity / InfoSec | 15.60 | 23 |
| Finance / Accounting | 12.80 | 21 |
| DevOps / Cloud | 11.10 | 15 |
| Legal | 9.90 | 13 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 234.60 | 381 |
| Global Business Mobility: Senior or Specialist Worker | 199.00 | 235 |
| Creative Worker | 1.50 | 3 |
| Global Business Mobility: Graduate Trainee | 1.00 | 1 |
| Government Authorised Exchange | 1.00 | 1 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Leadership | 169.40 | 242 |
| Standard | 164.80 | 233 |
| Senior | 68.50 | 98 |
| Entry | 34.40 | 48 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 329.00 | 329 |
| 0.50 recruiter_or_ambiguous | 72.00 | 144 |
| 0.20 substring_only | 27.60 | 138 |
| 0.85 fuzzy_strong | 8.50 | 10 |
| 0.92 alias_table | 0.00 | 0 |
