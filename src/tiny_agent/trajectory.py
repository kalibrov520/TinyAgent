from dataclasses import dataclass, field

from tiny_agent.response import LLMResponse


@dataclass
class TrajectoryStep:
    """One model response and its optional tool observation."""

    thought: str = ""
    action: dict | None = None
    observation: str | None = None
    answer: str | None = None
    metadata: dict | None = None


@dataclass
class Run:
    """One user query and the steps taken to answer it."""

    query: str
    steps: list[TrajectoryStep] = field(default_factory=list)


class Trajectory:
    """Record agent execution as a sequence of runs."""

    def __init__(self) -> None:
        self.runs: list[Run] = []

    def start(self, query: str) -> Run:
        """Start and return a new run for a query."""

        run = Run(query=query)
        self.runs.append(run)
        return run

    def record(
        self,
        response: LLMResponse,
        observation: str | None = None,
    ) -> TrajectoryStep:
        """Record and return a step in the current run."""

        if not self.runs:
            raise RuntimeError("Start a trajectory run before recording a step.")

        step = TrajectoryStep(
            thought=response.reasoning or "",
            metadata=response.metadata,
        )

        if observation is not None:
            step.action = response.tool_call
            step.observation = observation
        else:
            step.answer = response.content

        self.runs[-1].steps.append(step)
        return step
