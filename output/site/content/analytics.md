+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-08-06T04:26:22.872972+00:00"
last_research_at = "2026-08-06T04:26:22.872972+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-08-06T04:26:22.872972+00:00
Generated at: 2026-08-06T04:26:22.872972+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 145
- Unique matched jobs: 97
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 340
- Unique matched jobs: 97
- High-confidence unique jobs: 65
- Weighted matched jobs: 77.88
- Weighted high-confidence jobs: 64.68
- Weighted match rate: 22.91%
- Weighted high-confidence rate: 19.02%

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
| London | 34.85 | 46 |
| Manchester | 3.50 | 4 |
| Leeds | 2.50 | 3 |
| London, UK | 2.35 | 3 |
| Firswood, Manchester | 2.00 | 2 |
| Ocean Village, Southampton | 2.00 | 2 |
| Rusholme, Manchester | 2.00 | 2 |
| Glasgow, Scotland | 1.92 | 2 |
| Holbeck, Leeds | 1.92 | 2 |
| Bristol | 1.50 | 2 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Omnea | 16.00 | 16 |
| DX Network Services | 5.00 | 5 |
| Kier Group | 5.00 | 5 |
| Mixpanel | 4.00 | 4 |
| Adecco | 3.00 | 3 |
| Network Plus | 3.00 | 3 |
| eFinancialCareers | 3.00 | 3 |
| EY UK | 2.76 | 3 |
| Ramsay Health Care | 2.00 | 2 |
| Robert Walters | 2.00 | 2 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Other | 17.30 | 21 |
| Operations / Project Management | 14.79 | 18 |
| Data / AI | 9.52 | 12 |
| Finance / Accounting | 5.12 | 7 |
| Sales | 4.50 | 6 |
| Logistics / Supply Chain | 4.00 | 4 |
| Cybersecurity / InfoSec | 3.05 | 4 |
| Administration / Office | 2.70 | 4 |
| Transport | 2.50 | 4 |
| Creative / Media | 2.00 | 2 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 54.20 | 71 |
| Global Business Mobility: Senior or Specialist Worker | 19.42 | 21 |
| Global Business Mobility: Graduate Trainee | 3.26 | 4 |
| Creative Worker | 1.00 | 1 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 42.75 | 53 |
| Leadership | 27.73 | 34 |
| Senior | 7.20 | 9 |
| Entry | 0.20 | 1 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 61.00 | 61 |
| 0.50 recruiter_or_ambiguous | 7.00 | 14 |
| 0.92 alias_table | 3.68 | 4 |
| 0.85 fuzzy_strong | 3.40 | 4 |
| 0.20 substring_only | 2.80 | 14 |
