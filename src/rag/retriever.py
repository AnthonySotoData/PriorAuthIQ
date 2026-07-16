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

    Additional results are requested from ChromaDB so duplicate chunks can be
    removed without reducing the amount of useful context returned.
    """

    if not query.strip():
        raise ValueError("query cannot be empty")

    if n_results <= 0:
        raise ValueError("n_results must be greater than 0")

    expanded_result_count = max(n_results * 4, n_results)

    results = search_policy_chunks(
        query=query,
        payer=payer,
        n_results=expanded_result_count,
    )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    retrieved_chunks: list[dict[str, Any]] = []
    seen_chunks: set[tuple[str, str, str, int, int, str]] = set()

    for document, metadata, distance in zip(
        documents,
        metadatas,
        distances,
    ):
        duplicate_key = (
            str(metadata["payer"]),
            str(metadata["policy_title"]),
            str(metadata["source_file"]),
            int(metadata["page_number"]),
            int(metadata["chunk_index"]),
            str(document),
        )

        if duplicate_key in seen_chunks:
            continue

        seen_chunks.add(duplicate_key)

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

        if len(retrieved_chunks) == n_results:
            break

    return retrieved_chunks