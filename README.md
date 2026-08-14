# Tiny Agent

A small educational agent framework built around an OpenAI-compatible LLM endpoint.

## Package structure

```text
src/tiny_agent/
├── __init__.py    # Public imports
├── agent.py       # Agent orchestration
├── model_client.py # LLM API client
├── response.py    # Structured LLM response
└── trajectory.py  # Runs and recorded steps
```

The package name is `tiny_agent`; its main class is simply `Agent`:

```python
from tiny_agent import Agent, LLMClient

llm = LLMClient(model="gemma4:e4b")
agent = Agent(llm)

answer = agent.run("How's life?")
print(answer)
```

`Agent` coordinates the work, `LLMClient` talks to the model server, and
`Trajectory` records the resulting steps.

## Setup

The local virtual environment is in `.venv`. In PyCharm, select
`.venv/bin/python` as the project interpreter if it is not detected automatically.

Install the project and development tools when you are ready:

```bash
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

Run tests with:

```bash
pytest
```
