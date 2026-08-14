from dataclasses import dataclass

@dataclass
class Response:
    """Structured response from the LLM"""

    content: str = ""
    reasoning: str | None = None
    tool_call: dict | None = None
    metadata: dict | None = None
