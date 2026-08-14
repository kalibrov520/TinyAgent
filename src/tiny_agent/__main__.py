from tiny_agent.LLM import LLM
from tiny_agent.agent import Agent

# Re-initialize the LLM with the updated class
llm = LLM(model = "gemma4:e4b")

agent = Agent(llm = llm)
response = agent.run("what is 2 + 2")
print(response)