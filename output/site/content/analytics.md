+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-07-13T04:28:24.642792+00:00"
last_research_at = "2026-07-13T04:28:24.642792+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-07-13T04:28:24.642792+00:00
Generated at: 2026-07-13T04:28:24.642792+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 123
- Unique matched jobs: 89
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 284
- Unique matched jobs: 89
- High-confidence unique jobs: 63
- Weighted matched jobs: 72.55
- Weighted high-confidence jobs: 63.00
- Weighted match rate: 25.55%
- Weighted high-confidence rate: 22.18%

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
| London | 27.30 | 31 |
| Manchester | 11.70 | 13 |
| Isleworth, West London | 3.00 | 3 |
| Rusholme, Manchester | 3.00 | 3 |
| Liverpool | 2.40 | 4 |
| Easton, Bristol | 2.00 | 2 |
| Liverpool, Merseyside | 2.00 | 2 |
| Sydenham, Belfast | 2.00 | 2 |
| Bristol | 1.50 | 2 |
| Ocean Village, Southampton | 1.20 | 2 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| eFinancialCareers | 23.00 | 23 |
| AJ Bell | 8.00 | 8 |
| Uber eats | 5.00 | 5 |
| Network Plus | 3.00 | 3 |
| Sky | 3.00 | 3 |
| Teleperformance | 3.00 | 3 |
| Adecco | 2.00 | 2 |
| BAE Systems | 2.00 | 2 |
| The Gym Group | 2.00 | 2 |
| Witherslack Group | 2.00 | 2 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Other | 16.10 | 18 |
| Data / AI | 10.90 | 13 |
| Operations / Project Management | 9.45 | 12 |
| Finance / Accounting | 9.00 | 10 |
| Administration / Office | 4.20 | 6 |
| Cybersecurity / InfoSec | 4.00 | 4 |
| Banking / Financial Services | 3.00 | 3 |
| Customer Support / Success | 3.00 | 3 |
| Insurance | 3.00 | 3 |
| Software Engineering | 2.00 | 2 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 58.55 | 74 |
| Global Business Mobility: Senior or Specialist Worker | 8.50 | 9 |
| Creative Worker | 3.50 | 4 |
| Global Business Mobility: Graduate Trainee | 2.00 | 2 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 43.70 | 56 |
| Leadership | 18.95 | 22 |
| Senior | 9.70 | 10 |
| Entry | 0.20 | 1 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 63.00 | 63 |
| 0.50 recruiter_or_ambiguous | 4.00 | 8 |
| 0.20 substring_only | 3.00 | 15 |
| 0.85 fuzzy_strong | 2.55 | 3 |
| 0.92 alias_table | 0.00 | 0 |
