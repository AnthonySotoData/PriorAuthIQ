from src.rag.retriever import retrieve_policy_context

query = "When is durable medical equipment eligible for reimbursement?"

results = retrieve_policy_context(
    query=query,
    payer="AmeriHealth Caritas Ohio",
    n_results=3,
)

print(f"Query: {query}")
print(f"Retrieved chunks: {len(results)}")

for rank, result in enumerate(results, start=1):
    citation = result["citation"]

    print("=" * 80)
    print(f"Result {rank}")
    print(f"Distance: {result['distance']:.4f}")
    print(f"Payer: {citation['payer']}")
    print(f"Policy: {citation['policy_title']}")
    print(f"Page: {citation['page_number']}")
    print(f"Source: {citation['source_file']}")
    print(result["text"][:700])