from tiny_agent.model_client import LLMClient
from tiny_agent.trajectory import Trajectory


class Agent:
    """Coordinate an LLM client and record each run in a trajectory."""

    def __init__(self, llm: LLMClient) -> None:
        self.llm = llm
        self.trajectory = Trajectory()

    def run(self, task: str) -> str:
        """Run one task and return the model's answer."""

        self.trajectory.start(task)
        response = self.llm.generate([{"role": "user", "content": task}])
        self.trajectory.record(response)
        return response.content
