+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-05-14T06:32:19.090128+00:00"
last_research_at = "2026-05-14T06:32:19.090128+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-05-14T06:32:19.090128+00:00
Generated at: 2026-05-14T06:32:19.090128+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 161
- Unique matched jobs: 90
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 263
- Unique matched jobs: 90
- High-confidence unique jobs: 67
- Weighted matched jobs: 76.20
- Weighted high-confidence jobs: 67.00
- Weighted match rate: 28.97%
- Weighted high-confidence rate: 25.48%

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
| London, UK | 20.20 | 21 |
| Manchester | 4.20 | 5 |
| Belfast, Northern Ireland | 4.00 | 4 |
| Bristol, South West England | 3.00 | 3 |
| Glasgow, Scotland | 3.00 | 3 |
| Leeds | 3.00 | 3 |
| Manchester, Greater Manchester | 3.00 | 3 |
| Ocean Village, Southampton | 2.50 | 3 |
| London | 2.10 | 6 |
| Bolton, Greater Manchester | 2.00 | 2 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Hays | 33.00 | 33 |
| Aspire People Limited | 4.00 | 4 |
| BAE Systems | 4.00 | 4 |
| Witherslack Group | 4.00 | 4 |
| Kier Group | 3.00 | 3 |
| DX Network Services | 2.00 | 2 |
| Network Plus | 2.00 | 2 |
| Ramsay Health Care | 2.00 | 2 |
| Teleperformance | 2.00 | 2 |
| Tradewind Recruitment | 2.00 | 2 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Finance / Accounting | 27.00 | 27 |
| Other | 12.40 | 16 |
| Operations / Project Management | 9.50 | 11 |
| Administration / Office | 7.20 | 8 |
| Education / Teaching | 6.20 | 7 |
| Data / AI | 3.20 | 5 |
| Hospitality | 2.20 | 3 |
| HR / Recruitment | 1.35 | 2 |
| Nursing / Care | 1.20 | 2 |
| Allied Health | 1.00 | 1 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Global Business Mobility: Senior or Specialist Worker | 46.50 | 47 |
| Skilled Worker | 29.70 | 43 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 48.65 | 60 |
| Leadership | 22.35 | 24 |
| Senior | 3.20 | 4 |
| Entry | 2.00 | 2 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 67.00 | 67 |
| 0.50 recruiter_or_ambiguous | 5.50 | 11 |
| 0.20 substring_only | 2.00 | 10 |
| 0.85 fuzzy_strong | 1.70 | 2 |
| 0.92 alias_table | 0.00 | 0 |
