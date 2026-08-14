from tiny_agent.trajectory import Trajectory
from tiny_agent.LLM import LLM

class Agent:
    """A minimal, modular, and educational agent framework."""

    def __init__(self, llm: LLM):
        self.llm = llm
        self.memory = None # TODO
        self.tools = None # TODO
        self.planner = None # TODO

        self.trajectory = Trajectory()

    def run(self, task: str) -> str:
        """Run the agent on a task."""

        self.trajectory.initialize(task)
        return self._step(task)

    def _step(self, task: str) -> str:
        """Perform a single step."""

        message = [{"role": "user", "content": task}]
        response = self.llm.generate(message)
        self.trajectory.add(response)
        return response.content

    def _execute_action(self, action: str) -> str:
        """Execute a tool action."""

        # Placeholder for a tool action call and execution.
        return f"Executed action: {action}"
