from pydantic import BaseModel, Field


class Citation(BaseModel):
    payer: str
    policy_title: str
    source_file: str
    page_number: int
    chunk_index: int
    document_id: str


class RetrievedPolicyChunk(BaseModel):
    text: str
    distance: float
    citation: Citation


class PolicySearchRequest(BaseModel):
    query: str = Field(min_length=1)
    payer: str | None = None
    n_results: int = Field(default=3, ge=1, le=10)


class PolicySearchResponse(BaseModel):
    query: str
    payer: str | None
    results: list[RetrievedPolicyChunk]