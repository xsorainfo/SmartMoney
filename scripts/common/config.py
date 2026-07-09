
from __future__ import annotations

import os
from pathlib import Path

# ==========================
# Project Root
# ==========================

ROOT_DIR = Path(__file__).resolve().parents[2]

# ==========================
# Directories
# ==========================

DATA_DIR = ROOT_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

DOCS_DATA_DIR = ROOT_DIR / "docs" / "data"

LOG_DIR = ROOT_DIR / "logs"

# 自动创建目录
for path in (
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    DOCS_DATA_DIR,
    LOG_DIR,
):
    path.mkdir(parents=True, exist_ok=True)

# ==========================
# EDINET
# ==========================

EDINET_API_KEY = os.getenv("EDINET_API_KEY", "")

EDINET_BASE_URL = "https://api.edinet-fsa.go.jp/api/v2"

# ==========================
# HTTP
# ==========================

REQUEST_TIMEOUT = 30

USER_AGENT = "SmartMoney/0.1"
