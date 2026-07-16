from typing import Protocol

from src.models.ai_response import PriorAuthDecision


class LLMProvider(Protocol):
    """
    Interface implemented by every language-model provider used by PriorAuthIQ.

    This allows the application to switch between providers such as OpenAI,
    Azure OpenAI, Anthropic, or a local model without changing the retrieval
    and business-logic layers.
    """

    def generate(self, prompt: str) -> PriorAuthDecision:
        """
        Generate and validate a structured prior-authorization decision.
        """
        ...