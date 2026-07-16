from fastapi import APIRouter, HTTPException

from src.models.ai_response import PriorAuthDecision
from src.models.schemas import PolicySearchRequest
from src.services.prior_auth_service import PriorAuthService


router = APIRouter(
    prefix="/policies",
    tags=["Policy Search"],
)

service = PriorAuthService()


@router.post(
    "/search",
    response_model=PriorAuthDecision,
)
def search_policies(
    request: PolicySearchRequest,
) -> PriorAuthDecision:
    """
    Search payer policies and return an AI-generated,
    citation-backed authorization decision.
    """

    try:
        return service.answer_question(
            query=request.query,
            payer=request.payer,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc