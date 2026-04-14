from __future__ import annotations

from pathlib import Path

OUTPUT_ROOT = Path("output")
RAW_OUTPUT_DIR = OUTPUT_ROOT / "raw"
REPORTS_OUTPUT_DIR = OUTPUT_ROOT / "reports"
SITE_CONTENT_OUTPUT_DIR = OUTPUT_ROOT / "site" / "content"

DEFAULT_JOBS_OUTPUT = RAW_OUTPUT_DIR / "job_offers.json"
DEFAULT_SPONSORS_OUTPUT = RAW_OUTPUT_DIR / "registered_sponsors.json"
DEFAULT_MARKDOWN_OUTPUT = REPORTS_OUTPUT_DIR / "sponsored_jobs_report.md"
DEFAULT_MATCHED_JSON_OUTPUT = REPORTS_OUTPUT_DIR / "matched_sponsored_jobs.json"
DEFAULT_SITE_REPORT_OUTPUT = SITE_CONTENT_OUTPUT_DIR / "report.md"
