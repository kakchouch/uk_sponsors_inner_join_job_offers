+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-06-08T08:23:11.713779+00:00"
last_research_at = "2026-06-08T08:23:11.713779+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-06-08T08:23:11.713779+00:00
Generated at: 2026-06-08T08:23:11.713779+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 89
- Unique matched jobs: 69
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 156
- Unique matched jobs: 69
- High-confidence unique jobs: 32
- Weighted matched jobs: 43.28
- Weighted high-confidence jobs: 31.68
- Weighted match rate: 27.74%
- Weighted high-confidence rate: 20.31%

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
| London | 19.90 | 32 |
| East London | 4.00 | 8 |
| Bristol | 2.84 | 3 |
| Leeds | 2.50 | 4 |
| Manchester | 2.12 | 4 |
| Central London | 2.12 | 3 |
| North London | 2.00 | 2 |
| Liverpool | 1.50 | 3 |
| South East London | 1.20 | 2 |
| Easton, Bristol | 1.00 | 1 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| eFinancialCareers | 10.00 | 10 |
| Tradewind Recruitment | 5.00 | 5 |
| Lloyds Banking Group | 3.68 | 4 |
| Robert Half | 3.00 | 3 |
| Adecco | 2.00 | 2 |
| BAE Systems | 1.00 | 1 |
| BDO UK | 1.00 | 1 |
| Handle Recruitment | 1.00 | 1 |
| Network Plus | 1.00 | 1 |
| Salt Search | 1.00 | 1 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Other | 8.02 | 11 |
| Operations / Project Management | 7.94 | 12 |
| Finance / Accounting | 4.60 | 8 |
| Data / AI | 4.32 | 8 |
| Education / Teaching | 4.20 | 10 |
| Higher Education / Research | 3.00 | 3 |
| Administration / Office | 2.20 | 3 |
| Legal | 1.70 | 3 |
| Software Engineering | 1.20 | 2 |
| Allied Health | 1.00 | 1 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 32.10 | 57 |
| Global Business Mobility: Senior or Specialist Worker | 11.18 | 12 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 25.40 | 43 |
| Leadership | 15.18 | 22 |
| Senior | 2.70 | 4 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 28.00 | 28 |
| 0.50 recruiter_or_ambiguous | 7.00 | 14 |
| 0.20 substring_only | 4.60 | 23 |
| 0.92 alias_table | 3.68 | 4 |
| 0.85 fuzzy_strong | 0.00 | 0 |
