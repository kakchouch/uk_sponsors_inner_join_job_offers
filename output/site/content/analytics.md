+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-07-23T04:25:38.591642+00:00"
last_research_at = "2026-07-23T04:25:38.591642+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-07-23T04:25:38.591642+00:00
Generated at: 2026-07-23T04:25:38.591642+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 128
- Unique matched jobs: 85
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 273
- Unique matched jobs: 85
- High-confidence unique jobs: 52
- Weighted matched jobs: 65.10
- Weighted high-confidence jobs: 52.00
- Weighted match rate: 23.85%
- Weighted high-confidence rate: 19.05%

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
| London | 24.15 | 30 |
| Bristol | 5.55 | 7 |
| Manchester | 3.20 | 5 |
| Glasgow | 3.20 | 4 |
| Isleworth, West London | 3.00 | 3 |
| Leeds | 2.50 | 3 |
| London, UK | 2.25 | 4 |
| Firswood, Manchester | 2.00 | 2 |
| Ocean Village, Southampton | 2.00 | 2 |
| Altrincham, Greater Manchester | 1.00 | 1 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Southwark Council | 11.00 | 11 |
| Pearson Plc | 8.00 | 8 |
| Uber eats | 5.00 | 5 |
| Sky | 4.00 | 4 |
| Network Plus | 3.00 | 3 |
| Robert Half | 3.00 | 3 |
| MEARS GROUP PLC | 2.00 | 2 |
| Robert Walters | 2.00 | 2 |
| Witherslack Group | 2.00 | 2 |
| Adecco | 1.00 | 1 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Other | 22.65 | 26 |
| Operations / Project Management | 8.50 | 12 |
| Data / AI | 6.60 | 10 |
| Administration / Office | 4.50 | 6 |
| Nursing / Care | 3.40 | 5 |
| Creative / Media | 3.00 | 3 |
| Education / Teaching | 3.00 | 3 |
| Finance / Accounting | 2.20 | 5 |
| Skilled Trades | 2.00 | 3 |
| Real Estate / Property | 2.00 | 2 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 39.10 | 57 |
| Global Business Mobility: Senior or Specialist Worker | 20.50 | 21 |
| Creative Worker | 5.50 | 7 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 47.35 | 58 |
| Leadership | 12.35 | 20 |
| Senior | 3.40 | 5 |
| Entry | 2.00 | 2 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 52.00 | 52 |
| 0.50 recruiter_or_ambiguous | 6.50 | 13 |
| 0.85 fuzzy_strong | 3.40 | 4 |
| 0.20 substring_only | 3.20 | 16 |
| 0.92 alias_table | 0.00 | 0 |
