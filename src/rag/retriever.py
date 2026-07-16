from typing import Any

from src.rag.vector_store import search_policy_chunks


def retrieve_policy_context(
    query: str,
    payer: str | None = None,
    n_results: int = 3,
) -> list[dict[str, Any]]:
    """
    Retrieve relevant payer-policy chunks and normalize the ChromaDB response
    into a citation-friendly structure.
    """

    if not query.strip():
        raise ValueError("query cannot be empty")

    if n_results <= 0:
        raise ValueError("n_results must be greater than 0")

    results = search_policy_chunks(
        query=query,
        payer=payer,
        n_results=n_results,
    )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    retrieved_chunks: list[dict[str, Any]] = []

    for document, metadata, distance in zip(
        documents,
        metadatas,
        distances,
    ):
        retrieved_chunks.append(
            {
                "text": document,
                "distance": float(distance),
                "citation": {
                    "payer": metadata["payer"],
                    "policy_title": metadata["policy_title"],
                    "source_file": metadata["source_file"],
                    "page_number": metadata["page_number"],
                    "chunk_index": metadata["chunk_index"],
                    "document_id": metadata["document_id"],
                },
            }
        )

    return retrieved_chunks