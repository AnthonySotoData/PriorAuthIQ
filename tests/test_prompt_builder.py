from src.llm.prompt_builder import build_prompt


def test_build_prompt_includes_query_and_policy_context() -> None:
    retrieved_chunks = [
        {
            "text": "Durable medical equipment must be prescribed by a provider.",
            "distance": 0.12,
            "citation": {
                "payer": "Example Health Plan",
                "policy_title": "Durable Medical Equipment Policy",
                "source_file": "example_policy.pdf",
                "page_number": 2,
                "chunk_index": 0,
                "document_id": "example-document",
            },
        }
    ]

    prompt = build_prompt(
        query="Is prior authorization required?",
        retrieved_chunks=retrieved_chunks,
    )

    assert "Is prior authorization required?" in prompt
    assert "Example Health Plan" in prompt
    assert "Durable Medical Equipment Policy" in prompt
    assert "example_policy.pdf" in prompt
    assert "Page: 2" in prompt
    assert "Durable medical equipment must be prescribed by a provider." in prompt