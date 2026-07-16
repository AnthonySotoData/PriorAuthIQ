from openai import OpenAI

from src.config import settings
from src.llm.provider import LLMProvider
from src.models.ai_response import PriorAuthDecision


class OpenAIProvider(LLMProvider):
    """
    OpenAI implementation of the PriorAuthIQ language-model provider.
    """

    def __init__(self) -> None:
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model

    def generate(self, prompt: str) -> PriorAuthDecision:
        """
        Generate and validate a structured prior-authorization decision.
        """
        response = self.client.responses.parse(
            model=self.model,
            input=prompt,
            text_format=PriorAuthDecision,
        )

        if response.output_parsed is None:
            raise ValueError(
                "OpenAI did not return a valid structured response."
            )

        return response.output_parsed