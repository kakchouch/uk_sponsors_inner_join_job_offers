+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-08-20T04:00:00.233432+00:00"
last_research_at = "2026-08-20T04:00:00.233432+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-08-20T04:00:00.233432+00:00
Generated at: 2026-08-20T04:00:00.233432+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 225
- Unique matched jobs: 143
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 400
- Unique matched jobs: 143
- High-confidence unique jobs: 85
- Weighted matched jobs: 105.44
- Weighted high-confidence jobs: 84.84
- Weighted match rate: 26.36%
- Weighted high-confidence rate: 21.21%

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
| London | 33.10 | 45 |
| Bristol | 7.00 | 7 |
| Glasgow | 5.90 | 8 |
| Manchester | 5.00 | 6 |
| Leeds | 5.00 | 5 |
| Liverpool | 4.00 | 4 |
| Belfast, Northern Ireland | 3.95 | 8 |
| London, UK | 2.80 | 7 |
| Hillhead, Glasgow City Centre | 2.50 | 3 |
| Broadgate, Central London | 2.00 | 2 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Pearson Plc | 21.00 | 21 |
| eFinancialCareers | 9.00 | 9 |
| Uber eats | 7.00 | 7 |
| BAE Systems | 5.00 | 5 |
| iwoca | 5.00 | 5 |
| Kier Group | 4.00 | 4 |
| Robert Walters | 3.00 | 3 |
| Adecco | 2.00 | 2 |
| Busy Bees Nurseries | 2.00 | 2 |
| Teleperformance | 2.00 | 2 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Other | 30.60 | 37 |
| Operations / Project Management | 14.82 | 19 |
| Administration / Office | 11.00 | 15 |
| Data / AI | 6.90 | 13 |
| Cybersecurity / InfoSec | 6.50 | 7 |
| Software Engineering | 5.55 | 7 |
| DevOps / Cloud | 5.00 | 5 |
| Nursing / Care | 3.60 | 6 |
| Skilled Trades | 2.20 | 4 |
| Banking / Financial Services | 2.20 | 3 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 53.40 | 88 |
| Global Business Mobility: Senior or Specialist Worker | 42.50 | 44 |
| Global Business Mobility: Graduate Trainee | 8.34 | 9 |
| Global Business Mobility: UK Expansion Worker | 1.00 | 1 |
| Charity Worker | 0.20 | 1 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 70.70 | 89 |
| Leadership | 20.24 | 31 |
| Senior | 9.85 | 14 |
| Entry | 4.65 | 9 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 83.00 | 83 |
| 0.50 recruiter_or_ambiguous | 8.50 | 17 |
| 0.20 substring_only | 7.00 | 35 |
| 0.85 fuzzy_strong | 5.10 | 6 |
| 0.92 alias_table | 1.84 | 2 |
