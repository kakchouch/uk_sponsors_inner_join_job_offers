+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-09-03T08:05:34.988251+00:00"
last_research_at = "2026-09-03T08:05:34.988251+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-09-03T08:05:34.988251+00:00
Generated at: 2026-09-03T08:05:34.988251+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 314
- Unique matched jobs: 209
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 485
- Unique matched jobs: 209
- High-confidence unique jobs: 104
- Weighted matched jobs: 141.77
- Weighted high-confidence jobs: 103.92
- Weighted match rate: 29.23%
- Weighted high-confidence rate: 21.43%

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
| London | 62.00 | 88 |
| London, UK | 22.00 | 34 |
| Manchester | 11.60 | 14 |
| Glasgow, Scotland | 4.00 | 4 |
| Isleworth, West London | 3.00 | 3 |
| Liverpool | 2.90 | 5 |
| Bristol | 2.20 | 3 |
| London Office | 2.00 | 2 |
| Leeds | 2.00 | 6 |
| UK - London | 1.60 | 4 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Ambition Europe Limited | 13.00 | 13 |
| Anaplan | 12.00 | 12 |
| Flock | 7.00 | 7 |
| Robert Half | 6.00 | 6 |
| eFinancialCareers | 4.00 | 4 |
| Adecco | 3.00 | 3 |
| BAE Systems | 3.00 | 3 |
| Sky | 3.00 | 3 |
| Aircall | 2.00 | 2 |
| Airwallex | 2.00 | 2 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Operations / Project Management | 30.35 | 39 |
| Other | 19.80 | 37 |
| Finance / Accounting | 17.45 | 23 |
| Data / AI | 14.40 | 23 |
| Cybersecurity / InfoSec | 12.45 | 15 |
| Administration / Office | 7.65 | 12 |
| Software Engineering | 7.32 | 9 |
| Legal | 4.20 | 5 |
| Consulting | 3.50 | 4 |
| Sales | 2.65 | 6 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 93.35 | 151 |
| Global Business Mobility: Senior or Specialist Worker | 38.92 | 47 |
| Creative Worker | 5.00 | 6 |
| Global Business Mobility: Graduate Trainee | 3.00 | 3 |
| International Agreement | 1.00 | 1 |
| Government Authorised Exchange | 0.50 | 1 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Leadership | 64.45 | 78 |
| Standard | 57.22 | 97 |
| Senior | 15.35 | 21 |
| Entry | 4.75 | 13 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 103.00 | 103 |
| 0.50 recruiter_or_ambiguous | 20.50 | 41 |
| 0.20 substring_only | 11.40 | 57 |
| 0.85 fuzzy_strong | 5.95 | 7 |
| 0.92 alias_table | 0.92 | 1 |
