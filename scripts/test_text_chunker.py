from pathlib import Path

from src.ingestion.pdf_reader import extract_pages
from src.ingestion.text_chunker import chunk_pages

pdf_path = Path("data/sample_policies/sample_policy.pdf")

pages = extract_pages(str(pdf_path))
chunks = chunk_pages(pages)

print(f"Pages extracted: {len(pages)}")
print(f"Chunks created: {len(chunks)}")

for chunk in chunks[:3]:
    print("=" * 80)
    print(
        f"Page {chunk['page_number']} | "
        f"Chunk {chunk['chunk_index']} | "
        f"Characters: {len(chunk['text'])}"
    )
    print(chunk["text"][:500])