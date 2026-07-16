from pathlib import Path

import fitz


def extract_pages(pdf_path: str) -> list[dict[str, str | int]]:
    """
    Extract text and page metadata from a PDF document.
    """

    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    document = fitz.open(path)
    pages: list[dict[str, str | int]] = []

    try:
        for page_number, page in enumerate(document, start=1):
            text = page.get_text().strip()

            if text:
                pages.append(
                    {
                        "page_number": page_number,
                        "text": text,
                    }
                )
    finally:
        document.close()

    return pages