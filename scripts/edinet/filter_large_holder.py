from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from scripts.common.config import RAW_EDINET_DIR
from scripts.common.logger import get_logger

logger = get_logger(__name__)


# EDINET 表单代码（第一版）
TARGET_FORMS = {
    "030000",  # 大量保有報告書
    "030001",  # 変更報告書
    "030002",  # 訂正大量保有報告書
    "030003",  # 訂正変更報告書
}


def filter_documents(documents: list[dict]) -> list[dict]:
    """Filter large holder reports."""

    results: list[dict] = []

    for doc in documents:
        form_code = doc.get("formCode")

        if form_code in TARGET_FORMS:
            results.append(doc)

    return results


def main() -> None:

    target_date = date.today()

    folder: Path = RAW_EDINET_DIR / target_date.strftime("%Y-%m-%d")

    input_file = folder / "document_list.json"

    output_file = folder / "large_holder_list.json"

    if not input_file.exists():
        raise FileNotFoundError(input_file)

    with input_file.open("r", encoding="utf-8") as f:
        data = json.load(f)

    documents = data.get("results", [])

    logger.info("Total documents : %d", len(documents))

    holders = filter_documents(documents)

    logger.info("Large holder reports : %d", len(holders))

    with output_file.open("w", encoding="utf-8") as f:
        json.dump(
            holders,
            f,
            ensure_ascii=False,
            indent=2,
        )

    logger.info("Saved %s", output_file)


if __name__ == "__main__":
    main()
