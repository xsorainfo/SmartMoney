
from __future__ import annotations

"""
Logging utilities for SmartMoney.
"""

import logging
from pathlib import Path

from scripts.common.config import LOG_DIR

LOG_FILE: Path = LOG_DIR / "smartmoney.log"


def get_logger(name: str) -> logging.Logger:
    """
    Create or return a configured logger.

    Args:
        name:
            Logger name.

    Returns:
        logging.Logger
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File
    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger
