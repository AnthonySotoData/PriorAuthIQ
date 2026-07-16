from fastapi import APIRouter, HTTPException

from src.models.schemas import (
    PolicySearchRequest,
    PolicySearchResponse,
    RetrievedPolicyChunk,
)
from src.rag.retriever import retrieve_policy_context


router = APIRouter(
    prefix="/policies",
    tags=["Policy Search"],
)


@router.post(
    "/search",
    response_model=PolicySearchResponse,
)
def search_policies(
    request: PolicySearchRequest,
) -> PolicySearchResponse:
    """
    Search indexed payer policies and return semantically relevant,
    citation-ready text chunks.
    """

    try:
        results = retrieve_policy_context(
            query=request.query,
            payer=request.payer,
            n_results=request.n_results,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    return PolicySearchResponse(
        query=request.query,
        payer=request.payer,
        results=[
            RetrievedPolicyChunk(**result)
            for result in results
        ],
    )