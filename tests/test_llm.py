from tiny_agent import LLMClient


def test_parse_response() -> None:
    data = {
        "model": "test-model",
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": "Done",
                    "reasoning": "Answer directly.",
                    "tool_calls": [{"id": "call-1"}],
                }
            }
        ],
        "usage": {
            "prompt_tokens": 5,
            "completion_tokens": 2,
        },
    }

    response = LLMClient._parse_response(data)

    assert response.content == "Done"
    assert response.reasoning == "Answer directly."
    assert response.tool_call == {"id": "call-1"}
    assert response.metadata == {
        "model": "test-model",
        "prompt_tokens": 5,
        "completion_tokens": 2,
    }
