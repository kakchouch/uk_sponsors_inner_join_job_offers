# Market Analytics

<<<<<<< HEAD
Last research run (UTC): 2026-04-17T19:28:57.115923+00:00
Generated at: 2026-04-17T19:28:57.115923+00:00
=======
Last research run (UTC): 2026-04-17T09:58:32.431504+00:00
Generated at: 2026-04-17T09:58:32.431504+00:00
>>>>>>> 2ffe9be9d94467f612e18ea51e2dacfd87b1fb6e

## Scope

- Filtering keywords: No keyword filter
- Analytics are computed on unique jobs deduplicated by title + company + location.
- Every analytics entry, chart, and category table is weighted by the match quality score.
- A 1.00 exact match contributes 1.00 to analytics totals, while lower-confidence rows contribute proportionally less.
- Raw matched rows before deduplication: 155
- Unique matched jobs: 89
- Search locations: London, Glasgow, Manchester, Leeds, Liverpool, Bristol, Southampton, Brighton, Plymouth, Portsmouth, Belfast

## Overview

- Total jobs fetched: 236
- Unique matched jobs: 89
- High-confidence unique jobs: 71
- Weighted matched jobs: 77.05
- Weighted high-confidence jobs: 71.00
- Weighted match rate: 32.65%
- Weighted high-confidence rate: 30.08%

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
| London, UK | 19.20 | 20 |
| London | 17.50 | 22 |
| Manchester, Greater Manchester | 4.00 | 4 |
| Belfast, Northern Ireland | 3.00 | 3 |
| Bristol, South West England | 3.00 | 3 |
| Glasgow City Centre, Glasgow | 3.00 | 3 |
| Manchester | 2.85 | 3 |
| Bolton, Greater Manchester | 2.20 | 3 |
| Easton, Bristol | 2.00 | 2 |
| Glasgow, Scotland | 2.00 | 2 |

## Top Employers (High Confidence)

| Company | Weighted score | Raw jobs |
|---|---|---|
| Hays | 27.00 | 27 |
| eFinancialCareers | 12.00 | 12 |
| HAYS | 9.00 | 9 |
| BAE Systems | 3.00 | 3 |
| Adecco | 2.00 | 2 |
| Creative Support Ltd | 2.00 | 2 |
| Evri | 2.00 | 2 |
| NG Bailey | 2.00 | 2 |
| Ribbons and Reeves Limited | 2.00 | 2 |
| Witherslack Group | 2.00 | 2 |

## Top Job Title Families

| Title Family | Weighted score | Raw jobs |
|---|---|---|
| Finance / Accounting | 30.00 | 31 |
| Operations / Project Management | 9.90 | 12 |
| Education / Teaching | 4.80 | 8 |
| Banking / Financial Services | 4.00 | 4 |
| Data / AI | 3.90 | 6 |
| Transport | 3.50 | 4 |
| DevOps / Cloud | 3.00 | 3 |
| Security | 3.00 | 3 |
| Software Engineering | 3.00 | 3 |
| Real Estate / Property | 2.20 | 3 |

## Visa Routes

| Route | Weighted score | Raw jobs |
|---|---|---|
| Global Business Mobility: Senior or Specialist Worker | 48.00 | 49 |
| Skilled Worker | 29.05 | 40 |

## Title Seniority

| Seniority | Weighted score | Raw jobs |
|---|---|---|
| Standard | 35.05 | 42 |
| Leadership | 30.60 | 34 |
| Senior | 10.20 | 11 |
| Entry | 1.20 | 2 |

## Match Quality Breakdown

| Label | Weighted score | Raw jobs |
|---|---|---|
| 1.00 exact_normalized | 71.00 | 71 |
| 0.50 recruiter_or_ambiguous | 3.00 | 6 |
| 0.20 substring_only | 2.20 | 11 |
| 0.85 fuzzy_strong | 0.85 | 1 |
| 0.92 alias_table | 0.00 | 0 |
