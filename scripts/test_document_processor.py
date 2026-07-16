from pathlib import Path

from src.ingestion.document_processor import process_policy_document

pdf_path = Path("data/sample_policies/sample_policy.pdf")

chunks = process_policy_document(
    pdf_path=str(pdf_path),
    payer="AmeriHealth Caritas Ohio",
    policy_title="Durable Medical Equipment, Prosthetics, Orthotics, and Supplies",
)

print(f"Chunks created: {len(chunks)}")

for chunk in chunks[:2]:
    print("=" * 80)
    print(f"Payer: {chunk['payer']}")
    print(f"Policy: {chunk['policy_title']}")
    print(f"Source: {chunk['source_file']}")
    print(f"Page: {chunk['page_number']}")
    print(f"Chunk: {chunk['chunk_index']}")
    print(chunk["text"][:500])