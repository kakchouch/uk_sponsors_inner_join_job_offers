+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-10-12T10:51:42.204501+00:00"
last_research_at = "2026-10-12T10:51:42.204501+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-10-12T10:51:42.204501+00:00
Generated at: 2026-10-12T10:51:42.204501+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 234
- Unique matched jobs: 143
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 334
- Unique matched jobs: 143
- High-confidence unique jobs: 57
- Weighted matched jobs: 94.75
- Weighted high-confidence jobs: 57.00
- Weighted match rate: 28.37%
- Weighted high-confidence rate: 17.07%

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
| London | 32.30 | 56 |
| London, UK | 9.60 | 13 |
| Belfast, Northern Ireland | 5.70 | 7 |
| Manchester | 4.30 | 9 |
| Rusholme, Manchester | 3.00 | 3 |
| Bishops Waltham, Southampton | 2.00 | 2 |
| Ormeau, Belfast | 2.00 | 2 |
| UK - London | 2.00 | 2 |
| London, UK or Zurich | 1.50 | 3 |
| Greater Manchester | 1.50 | 2 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Uber eats | 9.00 | 9 |
| Forvis Mazars LLP | 3.00 | 3 |
| Network Plus | 3.00 | 3 |
| Adecco | 2.00 | 2 |
| Airwallex | 2.00 | 2 |
| Teleperformance | 2.00 | 2 |
| Tradewind Recruitment | 2.00 | 2 |
| Waymo | 2.00 | 2 |
| Aldridge Education | 1.00 | 1 |
| Alloy | 1.00 | 1 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Other | 25.35 | 33 |
| Operations / Project Management | 16.65 | 23 |
| Data / AI | 11.35 | 16 |
| Sales | 6.70 | 11 |
| Cybersecurity / InfoSec | 5.00 | 7 |
| Software Engineering | 4.30 | 10 |
| Finance / Accounting | 4.20 | 5 |
| Administration / Office | 3.95 | 7 |
| Skilled Trades | 2.55 | 4 |
| Creative / Media | 2.50 | 3 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 59.75 | 101 |
| Global Business Mobility: Senior or Specialist Worker | 28.00 | 32 |
| Global Business Mobility: Graduate Trainee | 4.50 | 5 |
| Creative Worker | 1.50 | 3 |
| Government Authorised Exchange | 1.00 | 2 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 42.90 | 68 |
| Leadership | 30.40 | 42 |
| Senior | 19.45 | 30 |
| Entry | 2.00 | 3 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 57.00 | 57 |
| 0.50 recruiter_or_ambiguous | 24.50 | 49 |
| 0.85 fuzzy_strong | 7.65 | 9 |
| 0.20 substring_only | 5.60 | 28 |
| 0.92 alias_table | 0.00 | 0 |
