from pathlib import Path

from src.ingestion.pdf_reader import extract_pages

pdf_path = Path("data/sample_policies/sample_policy.pdf")

pages = extract_pages(str(pdf_path))

print(f"Extracted {len(pages)} pages")

for page in pages[:2]:
    print("=" * 80)
    print(f"Page {page['page_number']}")
    print(page["text"][:1500])