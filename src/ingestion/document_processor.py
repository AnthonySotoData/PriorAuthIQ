from pathlib import Path
from typing import Any

from src.ingestion.pdf_reader import extract_pages
from src.ingestion.text_chunker import chunk_pages


def process_policy_document(
    pdf_path: str,
    payer: str,
    policy_title: str,
) -> list[dict[str, Any]]:
    """
    Extract and chunk a payer policy PDF while attaching document metadata
    needed for filtering, retrieval, and source citations.
    """

    path = Path(pdf_path)

    pages = extract_pages(str(path))
    chunks = chunk_pages(pages)

    for chunk in chunks:
        chunk["payer"] = payer
        chunk["policy_title"] = policy_title
        chunk["source_file"] = path.name

    return chunks