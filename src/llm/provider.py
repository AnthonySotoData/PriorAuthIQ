from typing import Protocol


class LLMProvider(Protocol):
    """
    Interface implemented by every language-model provider used by PriorAuthIQ.

    This allows the application to switch between providers such as OpenAI,
    Azure OpenAI, Anthropic, or a local model without changing the retrieval
    and business-logic layers.
    """

    def generate(self, prompt: str) -> str:
        """
        Generate a text response from the supplied prompt.
        """
        ...