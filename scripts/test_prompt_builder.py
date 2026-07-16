from src.llm.prompt_builder import build_prompt
from src.rag.retriever import retrieve_policy_context

query = "When is durable medical equipment eligible for reimbursement?"

retrieved_chunks = retrieve_policy_context(
    query=query,
    payer="AmeriHealth Caritas Ohio",
)

prompt = build_prompt(
    query=query,
    retrieved_chunks=retrieved_chunks,
)

print("=" * 80)
print(prompt)
print("=" * 80)