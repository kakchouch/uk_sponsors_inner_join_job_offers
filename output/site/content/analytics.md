+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-08-27T14:14:45.081186+00:00"
last_research_at = "2026-08-27T14:14:45.081186+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-08-27T14:14:45.081186+00:00
Generated at: 2026-08-27T14:14:45.081186+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 543
- Unique matched jobs: 452
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 644
- Unique matched jobs: 452
- High-confidence unique jobs: 50
- Weighted matched jobs: 139.07
- Weighted high-confidence jobs: 49.92
- Weighted match rate: 21.59%
- Weighted high-confidence rate: 7.75%

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
| London | 91.70 | 339 |
| London, UK | 5.20 | 8 |
| Bristol | 4.00 | 16 |
| Greater Manchester | 3.00 | 15 |
| Leeds | 2.80 | 6 |
| London Office | 2.40 | 4 |
| Manchester, Greater Manchester | 2.40 | 4 |
| Manchester | 2.10 | 5 |
| South East London, London | 1.75 | 4 |
| Belfast, Northern Ireland | 1.40 | 4 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Flock | 6.00 | 6 |
| Uber eats | 6.00 | 6 |
| Anthropic | 3.00 | 3 |
| Spaitial | 3.00 | 3 |
| Aircall | 2.00 | 2 |
| Aviva | 2.00 | 2 |
| DeepL | 2.00 | 2 |
| KINTEC RECRUITMENT LIMITED | 2.00 | 2 |
| Mistral.ai | 2.00 | 2 |
| Neko Health | 2.00 | 2 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Other | 37.70 | 121 |
| Operations / Project Management | 36.82 | 128 |
| Data / AI | 13.20 | 43 |
| Administration / Office | 6.55 | 24 |
| Software Engineering | 5.60 | 11 |
| Cybersecurity / InfoSec | 4.10 | 16 |
| Finance / Accounting | 4.00 | 17 |
| Sales | 3.80 | 8 |
| Education / Teaching | 3.20 | 16 |
| Legal | 2.60 | 9 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 102.65 | 406 |
| Global Business Mobility: Senior or Specialist Worker | 32.50 | 40 |
| Global Business Mobility: Graduate Trainee | 2.42 | 3 |
| Creative Worker | 1.50 | 3 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 61.85 | 204 |
| Leadership | 60.62 | 198 |
| Senior | 14.80 | 44 |
| Entry | 1.80 | 6 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 0.20 substring_only | 74.80 | 374 |
| 1.00 exact_normalized | 49.00 | 49 |
| 0.50 recruiter_or_ambiguous | 13.50 | 27 |
| 0.92 alias_table | 0.92 | 1 |
| 0.85 fuzzy_strong | 0.85 | 1 |
