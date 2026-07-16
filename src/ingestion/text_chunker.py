from typing import Any


def chunk_pages(
    pages: list[dict[str, Any]],
    chunk_size: int = 1200,
    chunk_overlap: int = 200,
) -> list[dict[str, Any]]:
    """
    Split extracted PDF pages into overlapping text chunks while preserving
    page-level metadata for later retrieval and citations.

    Chunk boundaries are adjusted to avoid splitting words when possible.
    """

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if chunk_overlap < 0:
        raise ValueError("chunk_overlap cannot be negative")

    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size")

    chunks: list[dict[str, Any]] = []

    for page in pages:
        text = " ".join(str(page["text"]).split())
        page_number = int(page["page_number"])
        start = 0
        chunk_index = 0

        while start < len(text):
            end = min(start + chunk_size, len(text))

            if end < len(text):
                last_space = text.rfind(" ", start, end)

                if last_space > start:
                    end = last_space

            chunk_text = text[start:end].strip()

            if chunk_text:
                chunks.append(
                    {
                        "page_number": page_number,
                        "chunk_index": chunk_index,
                        "text": chunk_text,
                    }
                )

            if end >= len(text):
                break

            next_start = max(0, end - chunk_overlap)

            if next_start > 0:
                next_space = text.find(" ", next_start)

                if next_space != -1:
                    next_start = next_space + 1

            start = next_start
            chunk_index += 1

    return chunks