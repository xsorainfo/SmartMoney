from __future__ import annotations

from datetime import date

import requests

from scripts.common.config import (
    EDINET_API_KEY,
    EDINET_BASE_URL,
    REQUEST_TIMEOUT,
    USER_AGENT,
)
from scripts.common.logger import get_logger

logger = get_logger(__name__)


class EdinetClient:
    """Client for EDINET API."""

    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": USER_AGENT,
            }
        )

    def get_document_list(self, target_date: date) -> dict:
        """
        Get document list for a specific date.

        Parameters
        ----------
        target_date : date

        Returns
        -------
        dict
            Raw JSON response.
        """

        url = f"{EDINET_BASE_URL}/documents.json"

        params = {
            "date": target_date.strftime("%Y-%m-%d"),
            "type": 2,
        }

        if EDINET_API_KEY:
            params["Subscription-Key"] = EDINET_API_KEY

        logger.info("Downloading document list: %s", target_date)

        response = self.session.get(
            url,
            params=params,
            timeout=REQUEST_TIMEOUT,
        )

        response.raise_for_status()

        return response.json()
