from src.llm.mock_provider import MockLLMProvider
from src.llm.prompt_builder import build_prompt
from src.models.ai_response import (
    PriorAuthDecision,
    SourceCitation,
)
from src.rag.retriever import retrieve_policy_context


class PriorAuthService:
    """
    Coordinates retrieval, prompt generation, and LLM inference.
    """

    def __init__(self) -> None:
        self.provider = MockLLMProvider()

    def answer_question(
        self,
        query: str,
        payer: str | None = None,
    ) -> PriorAuthDecision:
        retrieved_chunks = retrieve_policy_context(
            query=query,
            payer=payer,
        )

        prompt = build_prompt(
            query=query,
            retrieved_chunks=retrieved_chunks,
        )

        llm_response = self.provider.generate(prompt)

        citations = [
            SourceCitation(
                payer=chunk["citation"]["payer"],
                policy_title=chunk["citation"]["policy_title"],
                source_file=chunk["citation"]["source_file"],
                page_number=chunk["citation"]["page_number"],
            )
            for chunk in retrieved_chunks
        ]

        return PriorAuthDecision(
            authorization_required=None,
            confidence=0.0,
            summary=llm_response,
            reasoning=(
                "The mock provider does not perform policy interpretation. "
                "No authorization determination was made."
            ),
            coverage_requirements=[],
            missing_information=[
                "A real language model or rules engine is required to interpret "
                "the retrieved policy context."
            ],
            citations=citations,
        )