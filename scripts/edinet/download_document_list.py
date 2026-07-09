
from __future__ import annotations

import json
from datetime import date

from scripts.common.config import RAW_EDINET_DIR
from scripts.common.logger import get_logger
from scripts.services.edinet_client import EdinetClient

logger = get_logger(__name__)


def main() -> None:
    """Download today's EDINET document list."""

    target_date = date.today()

    client = EdinetClient()

    logger.info("Start downloading document list...")

    data = client.get_document_list(target_date)

    output_dir = RAW_EDINET_DIR / target_date.strftime("%Y-%m-%d")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "document_list.json"

    with output_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    logger.info("Saved to %s", output_file)
    logger.info("Finished.")


if __name__ == "__main__":
    main()
