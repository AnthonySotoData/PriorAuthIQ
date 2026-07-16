from src.llm.provider import LLMProvider


class MockLLMProvider(LLMProvider):
    """
    Temporary provider used while building and testing the application.

    The mock deliberately avoids making an authorization determination
    because it does not analyze policy language like a real LLM.
    """

    def generate(self, prompt: str) -> str:
        return (
            "The retrieved policy describes reimbursement requirements for "
            "durable medical equipment, but the supplied context does not "
            "explicitly establish whether prior authorization is required."
        )