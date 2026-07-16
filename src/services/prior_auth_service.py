from src.llm.openai_provider import OpenAIProvider
from src.llm.prompt_builder import build_prompt
from src.models.ai_response import PriorAuthDecision, SourceCitation
from src.rag.retriever import retrieve_policy_context


class PriorAuthService:
    """
    Coordinates retrieval, prompt generation, and LLM inference.
    """

    def __init__(self) -> None:
        self.provider = OpenAIProvider()

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

        decision = self.provider.generate(prompt)

        citations = [
            SourceCitation(
                payer=chunk["citation"]["payer"],
                policy_title=chunk["citation"]["policy_title"],
                source_file=chunk["citation"]["source_file"],
                page_number=chunk["citation"]["page_number"],
            )
            for chunk in retrieved_chunks
        ]

        return decision.model_copy(
            update={
                "citations": citations,
            }
        )