from tiny_agent import Agent, LLMResponse


class StubLLMClient:
    def generate(self, messages, tools=None):
        assert messages == [{"role": "user", "content": "Say hello"}]
        return LLMResponse(
            content="Hello!",
            reasoning="Respond to the greeting.",
            metadata={"model": "stub"},
        )


def test_agent_returns_answer_and_records_trajectory() -> None:
    agent = Agent(StubLLMClient())

    answer = agent.run("Say hello")

    assert answer == "Hello!"
    assert len(agent.trajectory.runs) == 1
    assert agent.trajectory.runs[0].query == "Say hello"
    assert agent.trajectory.runs[0].steps[0].answer == "Hello!"
    assert agent.trajectory.runs[0].steps[0].thought == "Respond to the greeting."
