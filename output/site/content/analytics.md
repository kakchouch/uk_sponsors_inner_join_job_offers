+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-10-01T10:10:03.739685+00:00"
last_research_at = "2026-10-01T10:10:03.739685+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-10-01T10:10:03.739685+00:00
Generated at: 2026-10-01T10:10:03.739685+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 239
- Unique matched jobs: 165
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 441
- Unique matched jobs: 165
- High-confidence unique jobs: 67
- Weighted matched jobs: 104.07
- Weighted high-confidence jobs: 66.92
- Weighted match rate: 23.60%
- Weighted high-confidence rate: 15.17%

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
| London | 31.85 | 53 |
| South East London | 10.00 | 10 |
| London, UK | 4.10 | 7 |
| Manchester | 3.55 | 5 |
| South East London, London | 3.25 | 5 |
| East London | 3.00 | 3 |
| UK - London | 3.00 | 3 |
| Leeds | 2.60 | 7 |
| Belfast, Northern Ireland | 2.50 | 3 |
| Charing Cross, Central London | 2.00 | 2 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Tradewind Recruitment | 13.00 | 13 |
| Hackajob Ltd | 4.00 | 4 |
| Network Plus | 4.00 | 4 |
| Airwallex | 3.00 | 3 |
| Adecco | 2.00 | 2 |
| Forvis Mazars LLP | 2.00 | 2 |
| Mphasis UK Ltd | 2.00 | 2 |
| Robert Walters | 2.00 | 2 |
| Scopely | 2.00 | 2 |
| celonis | 2.00 | 2 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Operations / Project Management | 22.87 | 31 |
| Other | 14.60 | 24 |
| Data / AI | 10.80 | 18 |
| Education / Teaching | 6.65 | 10 |
| Administration / Office | 6.45 | 9 |
| Skilled Trades | 6.20 | 9 |
| Finance / Accounting | 5.40 | 8 |
| Sales | 4.90 | 9 |
| Creative / Media | 3.70 | 5 |
| Software Engineering | 3.20 | 6 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 75.95 | 126 |
| Global Business Mobility: Senior or Specialist Worker | 21.42 | 29 |
| Creative Worker | 3.20 | 6 |
| Global Business Mobility: Graduate Trainee | 2.00 | 2 |
| Scale-up | 1.00 | 1 |
| Government Authorised Exchange | 0.50 | 1 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 54.65 | 89 |
| Leadership | 35.77 | 51 |
| Senior | 12.40 | 22 |
| Entry | 1.25 | 3 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 66.00 | 66 |
| 0.50 recruiter_or_ambiguous | 19.50 | 39 |
| 0.20 substring_only | 10.00 | 50 |
| 0.85 fuzzy_strong | 7.65 | 9 |
| 0.92 alias_table | 0.92 | 1 |
