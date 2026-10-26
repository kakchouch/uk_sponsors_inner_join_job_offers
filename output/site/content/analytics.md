+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-10-26T08:57:15.362772+00:00"
last_research_at = "2026-10-26T08:57:15.362772+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-10-26T08:57:15.362772+00:00
Generated at: 2026-10-26T08:57:15.362772+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 689
- Unique matched jobs: 417
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 811
- Unique matched jobs: 417
- High-confidence unique jobs: 224
- Weighted matched jobs: 299.95
- Weighted high-confidence jobs: 224.00
- Weighted match rate: 36.99%
- Weighted high-confidence rate: 27.62%

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
| London | 155.50 | 219 |
| Bristol | 33.20 | 46 |
| London, United Kingdom | 27.90 | 30 |
| Manchester | 7.85 | 8 |
| London Office | 7.20 | 8 |
| London, England, United Kingdom | 6.00 | 8 |
| London, UK | 4.75 | 10 |
| London, Greater London, United Kingdom | 4.00 | 4 |
| UK London, United Kingdom | 4.00 | 4 |
| Bristol; Cambridge | 3.00 | 4 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Palantir | 27.00 | 27 |
| Graphcore | 25.00 | 25 |
| Sparta Commodities | 10.00 | 10 |
| Nebius | 8.00 | 8 |
| Woven By Toyota | 7.00 | 7 |
| Uber eats | 6.00 | 6 |
| Ekimetrics | 5.00 | 5 |
| Logicmonitor | 5.00 | 5 |
| Robert Half | 5.00 | 5 |
| Sonarsource | 5.00 | 5 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Software Engineering | 59.50 | 71 |
| Other | 47.95 | 76 |
| Operations / Project Management | 47.50 | 68 |
| Data / AI | 37.85 | 48 |
| Sales | 20.10 | 25 |
| Finance / Accounting | 11.90 | 16 |
| Cybersecurity / InfoSec | 11.80 | 17 |
| Consulting | 8.70 | 13 |
| DevOps / Cloud | 8.50 | 11 |
| Administration / Office | 6.50 | 12 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 157.95 | 249 |
| Global Business Mobility: Senior or Specialist Worker | 138.50 | 164 |
| Creative Worker | 2.50 | 3 |
| Global Business Mobility: Graduate Trainee | 1.00 | 1 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 118.40 | 174 |
| Leadership | 97.45 | 132 |
| Senior | 51.10 | 63 |
| Entry | 33.00 | 48 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 224.00 | 224 |
| 0.50 recruiter_or_ambiguous | 52.50 | 105 |
| 0.20 substring_only | 15.80 | 79 |
| 0.85 fuzzy_strong | 7.65 | 9 |
| 0.92 alias_table | 0.00 | 0 |
