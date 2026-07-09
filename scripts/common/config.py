from __future__ import annotations

"""
Global configuration for SmartMoney.

All project paths and global settings should be defined here.
"""

import os
from pathlib import Path

# ==============================================================================
# Project Paths
# ==============================================================================

# SmartMoney/
ROOT_DIR: Path = Path(__file__).resolve().parents[2]

DATA_DIR: Path = ROOT_DIR / "data"

RAW_DATA_DIR: Path = DATA_DIR / "raw"

PROCESSED_DATA_DIR: Path = DATA_DIR / "processed"

DOCS_DIR: Path = ROOT_DIR / "docs"

DOCS_DATA_DIR: Path = DOCS_DIR / "data"

LOG_DIR: Path = ROOT_DIR / "logs"

TEMP_DIR: Path = ROOT_DIR / "temp"

# Automatically create directories
for directory in (
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    DOCS_DATA_DIR,
    LOG_DIR,
    TEMP_DIR,
):
    directory.mkdir(parents=True, exist_ok=True)

# ==============================================================================
# EDINET
# ==============================================================================

EDINET_API_KEY: str = os.getenv("EDINET_API_KEY", "")

EDINET_BASE_URL: str = "https://api.edinet-fsa.go.jp/api/v2"

# ==============================================================================
# HTTP
# ==============================================================================

REQUEST_TIMEOUT: int = 30

USER_AGENT: str = "SmartMoney/0.1 (+https://github.com)"

# ==============================================================================
# GitHub Pages
# ==============================================================================

LATEST_JSON: Path = DOCS_DATA_DIR / "latest.json"

HISTORY_JSON: Path = DOCS_DATA_DIR / "history.json"

EVENTS_JSON: Path = DOCS_DATA_DIR / "events.json"

INSTITUTIONS_JSON: Path = DOCS_DATA_DIR / "institutions.json"

SCORES_JSON: Path = DOCS_DATA_DIR / "scores.json"

# ==============================================================================
# Raw EDINET
# ==============================================================================

RAW_EDINET_DIR: Path = RAW_DATA_DIR / "edinet"

RAW_EDINET_DIR.mkdir(parents=True, exist_ok=True)
