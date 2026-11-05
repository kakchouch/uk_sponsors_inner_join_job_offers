+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-11-05T10:57:39.824185+00:00"
last_research_at = "2026-11-05T10:57:39.824185+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-11-05T10:57:39.824185+00:00
Generated at: 2026-11-05T10:57:39.824185+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 641
- Unique matched jobs: 429
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 755
- Unique matched jobs: 429
- High-confidence unique jobs: 220
- Weighted matched jobs: 300.55
- Weighted high-confidence jobs: 220.00
- Weighted match rate: 39.81%
- Weighted high-confidence rate: 29.14%

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
| London | 192.30 | 276 |
| London - JJ Mack | 22.00 | 22 |
| London, UK | 12.70 | 19 |
| Manchester | 7.70 | 10 |
| London, England, United Kingdom | 6.00 | 10 |
| London Office | 6.00 | 7 |
| Glasgow | 4.70 | 8 |
| UK - London | 4.00 | 4 |
| Belfast, Northern Ireland | 3.70 | 5 |
| Leeds | 2.20 | 3 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Fractile | 22.00 | 22 |
| Flock | 8.00 | 8 |
| Quantexa | 7.00 | 7 |
| Uber eats | 7.00 | 7 |
| 9Fin | 6.00 | 6 |
| ClaimSorted | 6.00 | 6 |
| Kpler | 6.00 | 6 |
| Ripple | 6.00 | 6 |
| Australasian Recruitment Company | 5.00 | 5 |
| Nebius | 5.00 | 5 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Operations / Project Management | 72.25 | 103 |
| Other | 55.45 | 79 |
| Sales | 28.35 | 34 |
| Data / AI | 26.20 | 37 |
| Software Engineering | 23.50 | 31 |
| Administration / Office | 14.10 | 19 |
| Marketing | 10.10 | 12 |
| Legal | 8.35 | 15 |
| DevOps / Cloud | 7.90 | 12 |
| HR / Recruitment | 7.70 | 14 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 207.35 | 315 |
| Global Business Mobility: Senior or Specialist Worker | 87.50 | 106 |
| Global Business Mobility: Graduate Trainee | 4.00 | 4 |
| Creative Worker | 1.50 | 3 |
| Charity Worker | 0.20 | 1 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 126.10 | 176 |
| Leadership | 111.15 | 159 |
| Senior | 57.00 | 84 |
| Entry | 6.30 | 10 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 220.00 | 220 |
| 0.50 recruiter_or_ambiguous | 44.00 | 88 |
| 0.20 substring_only | 20.40 | 102 |
| 0.85 fuzzy_strong | 16.15 | 19 |
| 0.92 alias_table | 0.00 | 0 |
