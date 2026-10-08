+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-10-08T10:36:43.776551+00:00"
last_research_at = "2026-10-08T10:36:43.776551+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-10-08T10:36:43.776551+00:00
Generated at: 2026-10-08T10:36:43.776551+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 239
- Unique matched jobs: 158
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 387
- Unique matched jobs: 158
- High-confidence unique jobs: 60
- Weighted matched jobs: 92.00
- Weighted high-confidence jobs: 60.00
- Weighted match rate: 23.77%
- Weighted high-confidence rate: 15.50%

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
| London | 34.00 | 55 |
| Manchester | 6.20 | 8 |
| London, UK | 4.05 | 5 |
| Ocean Village, Southampton | 2.70 | 4 |
| Southampton, Hampshire | 2.50 | 4 |
| London, England - Hybrid | 2.00 | 4 |
| London, Greater London, United Kingdom | 2.00 | 4 |
| UK - London | 1.80 | 9 |
| Belfast, Northern Ireland | 1.70 | 3 |
| Leeds | 1.60 | 5 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| eFinancialCareers | 7.00 | 7 |
| Uber eats | 6.00 | 6 |
| Robert Walters | 4.00 | 4 |
| Tradewind Recruitment | 4.00 | 4 |
| Ambition Europe Limited | 3.00 | 3 |
| BAE Systems | 3.00 | 3 |
| Avepoint | 2.00 | 2 |
| Forvis Mazars LLP | 2.00 | 2 |
| Genomics | 2.00 | 2 |
| Hackajob Ltd | 2.00 | 2 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Other | 19.50 | 29 |
| Data / AI | 12.30 | 19 |
| Operations / Project Management | 11.60 | 25 |
| Sales | 7.30 | 14 |
| Education / Teaching | 6.20 | 7 |
| Banking / Financial Services | 5.00 | 5 |
| Software Engineering | 4.50 | 9 |
| Transport | 4.40 | 7 |
| Administration / Office | 4.20 | 6 |
| Finance / Accounting | 3.90 | 6 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 52.50 | 107 |
| Global Business Mobility: Senior or Specialist Worker | 34.50 | 46 |
| Global Business Mobility: Graduate Trainee | 5.00 | 5 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 51.55 | 87 |
| Leadership | 30.00 | 52 |
| Senior | 8.05 | 14 |
| Entry | 2.40 | 5 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 60.00 | 60 |
| 0.50 recruiter_or_ambiguous | 18.50 | 37 |
| 0.20 substring_only | 11.80 | 59 |
| 0.85 fuzzy_strong | 1.70 | 2 |
| 0.92 alias_table | 0.00 | 0 |
