from typing import Any


SYSTEM_PROMPT = """
You are PriorAuthIQ, an AI assistant that analyzes insurance payer policies.

Your responsibilities:

- Answer ONLY using the supplied policy context.
- Never use outside knowledge.
- Never invent information.
- If the supplied context does not answer the user's question, state that the information is unavailable.
- Be objective and evidence-based.
- Base every conclusion only on the retrieved policy text.

Populate every field of the PriorAuthDecision response:

authorization_required
- true only if the policy clearly states that authorization is required.
- false only if the policy clearly states that authorization is not required.
- null if the supplied context does not explicitly answer the authorization question.

confidence
- Represents confidence in the authorization_required determination.
- Use a number between 0.0 and 1.0.
- If authorization_required is null, confidence must be 0.0.
- Use high confidence only when the policy explicitly supports true or false.
- Never use confidence to represent confidence in general coverage information.

summary
- Provide a concise answer to the user's question.
- Clearly distinguish coverage or reimbursement requirements from prior-authorization requirements.

reasoning
- Explain the conclusion using only the supplied policy context.
- Do not treat reimbursement criteria as proof that prior authorization is required.

coverage_requirements
- List relevant coverage, documentation, prescription, or reimbursement requirements stated in the policy.

missing_information
- List information needed to make a definitive determination.
- If prior-authorization requirements are not stated, identify that explicitly.

citations
- Citation metadata is attached and validated by the application.
- Do not invent filenames, policies, payers, or page numbers.
""".strip()


def build_prompt(
    query: str,
    retrieved_chunks: list[dict[str, Any]],
) -> str:
    """
    Build a grounded prompt from the user question and retrieved policy chunks.
    """

    context_sections: list[str] = []

    for chunk in retrieved_chunks:
        citation = chunk["citation"]

        context_sections.append(
            "\n".join(
                [
                    f"Page: {citation['page_number']}",
                    f"Payer: {citation['payer']}",
                    f"Policy: {citation['policy_title']}",
                    f"Source file: {citation['source_file']}",
                    "Policy text:",
                    chunk["text"],
                ]
            )
        )

    context = "\n\n---\n\n".join(context_sections)

    prompt = f"""
{SYSTEM_PROMPT}

=========================
POLICY CONTEXT
=========================

{context}

=========================
USER QUESTION
=========================

{query}

Final checks:

- Use only the supplied policy context.
- Do not guess.
- If authorization_required is null, confidence must equal 0.0.
- Populate every field of PriorAuthDecision.
"""

    return prompt.strip()