+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-05-25T07:59:15.363280+00:00"
last_research_at = "2026-05-25T07:59:15.363280+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-05-25T07:59:15.363280+00:00
Generated at: 2026-05-25T07:59:15.363280+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 277
- Unique matched jobs: 147
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 322
- Unique matched jobs: 147
- High-confidence unique jobs: 116
- Weighted matched jobs: 127.75
- Weighted high-confidence jobs: 116.00
- Weighted match rate: 39.67%
- Weighted high-confidence rate: 36.02%

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
| Leeds | 13.70 | 15 |
| Manchester | 13.15 | 16 |
| London, UK | 11.00 | 11 |
| Belfast, Northern Ireland | 10.00 | 10 |
| Bristol | 10.00 | 10 |
| Glasgow | 9.00 | 9 |
| Liverpool | 9.00 | 9 |
| London | 8.20 | 17 |
| Glasgow, Scotland | 6.00 | 6 |
| Langbank, Port Glasgow | 3.00 | 3 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Pearson Plc | 43.00 | 43 |
| Hays | 37.00 | 37 |
| NG Bailey | 9.00 | 9 |
| Tradewind Recruitment | 6.00 | 6 |
| BAE Systems | 5.00 | 5 |
| HAYS | 3.00 | 3 |
| Aspire People Limited | 2.00 | 2 |
| Uber eats | 2.00 | 2 |
| eFinancialCareers | 2.00 | 2 |
| BDO UK | 1.00 | 1 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Other | 29.20 | 30 |
| Marketing | 26.20 | 27 |
| Finance / Accounting | 18.70 | 20 |
| Administration / Office | 11.05 | 12 |
| Operations / Project Management | 10.20 | 16 |
| Cybersecurity / InfoSec | 7.00 | 7 |
| Skilled Trades | 6.20 | 8 |
| Education / Teaching | 4.20 | 5 |
| Data / AI | 3.60 | 8 |
| Banking / Financial Services | 2.00 | 2 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 123.25 | 138 |
| Global Business Mobility: Senior or Specialist Worker | 4.50 | 9 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 76.25 | 86 |
| Leadership | 39.60 | 47 |
| Senior | 8.90 | 11 |
| Entry | 3.00 | 3 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 116.00 | 116 |
| 0.50 recruiter_or_ambiguous | 6.00 | 12 |
| 0.20 substring_only | 3.20 | 16 |
| 0.85 fuzzy_strong | 2.55 | 3 |
| 0.92 alias_table | 0.00 | 0 |
