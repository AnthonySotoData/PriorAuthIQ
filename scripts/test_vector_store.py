from pathlib import Path

from src.ingestion.document_processor import process_policy_document
from src.rag.vector_store import get_policy_collection, index_policy_chunks

pdf_path = Path("data/sample_policies/sample_policy.pdf")

chunks = process_policy_document(
    pdf_path=str(pdf_path),
    payer="AmeriHealth Caritas Ohio",
    policy_title="Durable Medical Equipment, Prosthetics, Orthotics, and Supplies",
)

indexed_count = index_policy_chunks(
    chunks=chunks,
    document_id="amerihealth-ohio-dmepos-rpc-0074-7700",
)

collection = get_policy_collection()

print(f"Chunks indexed: {indexed_count}")
print(f"Collection count: {collection.count()}")