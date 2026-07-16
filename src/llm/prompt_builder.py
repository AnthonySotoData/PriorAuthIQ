from typing import Any


SYSTEM_PROMPT = """
You are PriorAuthIQ.

You answer questions about insurance payer policies.

Rules:

1. Answer ONLY using the provided policy context.

2. Never invent information.

3. If the policy does not answer the question,
   explicitly say the information is unavailable.

4. Always cite the supporting page numbers.

5. Keep answers concise and professional.
""".strip()


def build_prompt(
    query: str,
    retrieved_chunks: list[dict[str, Any]],
) -> str:
    """
    Build the prompt sent to the language model.
    """

    context = ""

    for chunk in retrieved_chunks:
        citation = chunk["citation"]

        context += (
            f"\n\n"
            f"Page {citation['page_number']}\n"
            f"{chunk['text']}"
        )

    prompt = f"""
{SYSTEM_PROMPT}

Policy Context:

{context}

Question:

{query}

Answer:
"""

    return prompt.strip()