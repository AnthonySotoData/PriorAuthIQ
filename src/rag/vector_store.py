from pathlib import Path
from typing import Any

import chromadb
from chromadb.api.models.Collection import Collection
from chromadb.utils.embedding_functions import (
    SentenceTransformerEmbeddingFunction,
)


VECTOR_STORE_PATH = Path("data/vector_store")
COLLECTION_NAME = "payer_policies"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

embedding_function = SentenceTransformerEmbeddingFunction(
    model_name=EMBEDDING_MODEL_NAME,
    device="cpu",
    normalize_embeddings=True,
)


def get_policy_collection() -> Collection:
    """
    Create or load the persistent ChromaDB collection used to store
    payer-policy text chunks and their associated citation metadata.
    """

    VECTOR_STORE_PATH.mkdir(parents=True, exist_ok=True)

    client = chromadb.PersistentClient(path=str(VECTOR_STORE_PATH))

    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_function,
        metadata={
            "description": "PriorAuthIQ payer policy knowledge base"
        },
    )


def index_policy_chunks(
    chunks: list[dict[str, Any]],
    document_id: str,
) -> int:
    """
    Add processed policy chunks to ChromaDB.

    Each chunk receives a unique ID and retains metadata used for filtering
    and source citations.
    """

    if not chunks:
        return 0

    collection = get_policy_collection()

    ids: list[str] = []
    documents: list[str] = []
    metadatas: list[dict[str, str | int]] = []

    for chunk in chunks:
        chunk_id = (
            f"{document_id}"
            f"-page-{chunk['page_number']}"
            f"-chunk-{chunk['chunk_index']}"
        )

        ids.append(chunk_id)
        documents.append(str(chunk["text"]))
        metadatas.append(
            {
                "document_id": document_id,
                "payer": str(chunk["payer"]),
                "policy_title": str(chunk["policy_title"]),
                "source_file": str(chunk["source_file"]),
                "page_number": int(chunk["page_number"]),
                "chunk_index": int(chunk["chunk_index"]),
            }
        )

    collection.upsert(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
    )

    return len(ids)


def search_policy_chunks(
    query: str,
    n_results: int = 3,
    payer: str | None = None,
) -> dict[str, Any]:
    """
    Search the policy knowledge base for semantically relevant chunks.

    An optional payer filter can restrict results to one insurance payer.
    """

    collection = get_policy_collection()

    where_filter = {"payer": payer} if payer else None

    return collection.query(
        query_texts=[query],
        n_results=n_results,
        where=where_filter,
        include=["documents", "metadatas", "distances"],
    )