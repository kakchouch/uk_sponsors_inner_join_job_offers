+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-08-10T04:55:07.814894+00:00"
last_research_at = "2026-08-10T04:55:07.814894+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-08-10T04:55:07.814894+00:00
Generated at: 2026-08-10T04:55:07.814894+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 176
- Unique matched jobs: 111
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 361
- Unique matched jobs: 111
- High-confidence unique jobs: 60
- Weighted matched jobs: 77.07
- Weighted high-confidence jobs: 59.92
- Weighted match rate: 21.35%
- Weighted high-confidence rate: 16.60%

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
| London | 39.40 | 54 |
| Leeds | 4.00 | 5 |
| Glasgow | 3.70 | 5 |
| Soho, West London | 2.00 | 2 |
| South East London, London | 2.00 | 2 |
| Hilsea, Portsmouth | 1.70 | 3 |
| Belfast, Northern Ireland | 1.50 | 2 |
| Reading (London) | 1.20 | 6 |
| Liverpool | 1.20 | 2 |
| Manchester | 1.20 | 2 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| eFinancialCareers | 16.00 | 16 |
| Adecco | 4.00 | 4 |
| Ambition Europe Limited | 3.00 | 3 |
| BAE Systems | 3.00 | 3 |
| Kier Group | 3.00 | 3 |
| Uber eats | 3.00 | 3 |
| Gocardless | 2.00 | 2 |
| Harvey Nash | 2.00 | 2 |
| Robert Walters | 2.00 | 2 |
| Teleperformance Ltd | 2.00 | 2 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Operations / Project Management | 16.40 | 21 |
| Other | 13.05 | 19 |
| Finance / Accounting | 12.12 | 18 |
| Data / AI | 5.00 | 10 |
| Banking / Financial Services | 4.00 | 4 |
| Administration / Office | 3.60 | 6 |
| Insurance | 3.00 | 3 |
| Skilled Trades | 2.50 | 4 |
| Transport | 2.00 | 4 |
| Customer Support / Success | 2.00 | 2 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 51.95 | 82 |
| Global Business Mobility: Senior or Specialist Worker | 18.50 | 19 |
| Global Business Mobility: Graduate Trainee | 4.42 | 5 |
| Creative Worker | 2.20 | 5 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 35.65 | 56 |
| Leadership | 30.92 | 43 |
| Senior | 10.50 | 12 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 59.00 | 59 |
| 0.50 recruiter_or_ambiguous | 10.50 | 21 |
| 0.20 substring_only | 5.80 | 29 |
| 0.92 alias_table | 0.92 | 1 |
| 0.85 fuzzy_strong | 0.85 | 1 |
