from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from config import MODEL_NAME


checkpoint = InMemorySaver()

model = create_agent(
    model=MODEL_NAME,
    tools=[],
    checkpointer=checkpoint
)