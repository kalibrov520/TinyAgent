from dataclasses import dataclass


@dataclass
class LLMResponse:
    """Structured result returned by an LLM client."""

    content: str = ""
    reasoning: str | None = None
    tool_call: dict | None = None
    metadata: dict | None = None
