import json
import urllib.request
from typing import Any

from tiny_agent.response import LLMResponse


class LLMClient:
    """Client for an OpenAI-compatible chat-completions endpoint."""

    def __init__(
        self,
        model: str,
        base_url: str = "http://localhost:11434/v1",
        api_key: str = "no_key",
        reasoning: bool = False,
    ) -> None:
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.reasoning = reasoning

    def generate(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
    ) -> LLMResponse:
        """Generate a structured response from a list of chat messages."""

        body: dict[str, Any] = {
            "model": self.model,
            "messages": messages,
        }

        if tools:
            body["tools"] = tools
        if not self.reasoning:
            body["reasoning_effort"] = "none"

        request = urllib.request.Request(
            f"{self.base_url}/chat/completions",
            data=json.dumps(body).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            },
        )

        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read())

        return self._parse_response(data)

    @staticmethod
    def _parse_response(data: dict[str, Any]) -> LLMResponse:
        """Convert a chat-completions response into the package response type."""

        message = data["choices"][0]["message"]
        tool_calls = message.get("tool_calls") or []
        usage = data.get("usage", {})

        return LLMResponse(
            content=message.get("content") or "",
            reasoning=message.get("reasoning"),
            tool_call=tool_calls[0] if tool_calls else None,
            metadata={
                "model": data.get("model"),
                "prompt_tokens": usage.get("prompt_tokens"),
                "completion_tokens": usage.get("completion_tokens"),
            },
        )
