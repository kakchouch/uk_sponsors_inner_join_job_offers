+++
title = "Market Analytics"
description = "Deduplicated, quality-score-weighted market analytics for the latest sponsor-matched UK job run."
lastmod = "2026-04-19T17:44:43.443926+00:00"
last_research_at = "2026-04-19T17:44:43.443926+00:00"
+++

# Market Analytics

Last research run (UTC): 2026-04-19T17:44:43.443926+00:00
Generated at: 2026-04-19T17:44:43.443926+00:00

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 151
- Unique matched jobs: 83

## Overview

- Total jobs fetched: 998
- Unique matched jobs: 83
- High-confidence unique jobs: 11
- Weighted matched jobs: 34.70
- Weighted high-confidence jobs: 11.00
- Weighted match rate: 3.48%
- Weighted high-confidence rate: 1.10%

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
| Berlin | 5.90 | 13 |
| Munich | 2.20 | 7 |
| Hamburg | 2.00 | 6 |
| Frankfurt am Main | 1.70 | 3 |
| Munich, Bavaria, Germany | 1.40 | 3 |
| Essen | 1.00 | 2 |
| Halle (Saale) | 1.00 | 2 |
| Holzminden | 1.00 | 1 |
| Köln, North Rhine-Westphalia, Germany | 1.00 | 1 |
| Ludwigsburg | 1.00 | 1 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Veeva Systems | 2.00 | 2 |
| Accenture | 1.00 | 1 |
| Catapult Sports | 1.00 | 1 |
| Instagrid | 1.00 | 1 |
| NFON | 1.00 | 1 |
| Options Group | 1.00 | 1 |
| Ping Identity | 1.00 | 1 |
| SYMRISE | 1.00 | 1 |
| binderholz | 1.00 | 1 |
| homie | 1.00 | 1 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Other | 13.20 | 31 |
| Operations / Project Management | 5.80 | 18 |
| Software Engineering | 4.40 | 9 |
| Data / AI | 2.60 | 6 |
| Cybersecurity / InfoSec | 2.00 | 2 |
| Consulting | 1.20 | 2 |
| Legal | 1.00 | 1 |
| Sales | 1.00 | 1 |
| DevOps / Cloud | 0.70 | 2 |
| HR / Recruitment | 0.70 | 2 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Skilled Worker | 24.30 | 65 |
| Global Business Mobility: Senior or Specialist Worker | 8.70 | 14 |
| Global Business Mobility: Graduate Trainee | 1.00 | 2 |
| Creative Worker | 0.50 | 1 |
| Charity Worker | 0.20 | 1 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 24.40 | 51 |
| Leadership | 6.30 | 19 |
| Senior | 3.60 | 11 |
| Entry | 0.40 | 2 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 0.50 recruiter_or_ambiguous | 15.50 | 31 |
| 1.00 exact_normalized | 11.00 | 11 |
| 0.20 substring_only | 8.20 | 41 |
| 0.85 fuzzy_strong | 0.00 | 0 |
| 0.92 alias_table | 0.00 | 0 |
