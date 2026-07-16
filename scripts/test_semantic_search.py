from src.rag.vector_store import search_policy_chunks

query = "When is durable medical equipment eligible for reimbursement?"

results = search_policy_chunks(
    query=query,
    n_results=3,
    payer="AmeriHealth Caritas Ohio",
)

documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]

print(f"Query: {query}")

for rank, (document, metadata, distance) in enumerate(
    zip(documents, metadatas, distances),
    start=1,
):
    print("=" * 80)
    print(f"Result {rank}")
    print(f"Distance: {distance:.4f}")
    print(f"Payer: {metadata['payer']}")
    print(f"Policy: {metadata['policy_title']}")
    print(f"Page: {metadata['page_number']}")
    print(f"Source: {metadata['source_file']}")
    print(document[:700])