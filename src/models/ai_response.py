from pydantic import BaseModel


class SourceCitation(BaseModel):
    payer: str
    policy_title: str
    source_file: str
    page_number: int


class PriorAuthDecision(BaseModel):
    authorization_required: bool | None

    confidence: float

    summary: str

    reasoning: str

    coverage_requirements: list[str]

    missing_information: list[str]

    citations: list[SourceCitation]