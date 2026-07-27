#refer tutorial https://www.youtube.com/watch?v=GAyNvq6Ayps
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

# 1. Define a tool the agent can use
@tool
def get_current_weather(location: str) -> str:
    """Get the current weather for a given location."""
    return f"The weather in {location} is sunny and 28°C."

tools = [get_current_weather]

# 2. Connect to local Ollama (use a model that supports tool calling)
model = ChatOllama(model="qwen2.5", temperature=0)

# 3. Create and run the ReAct Agent
agent_executor = create_react_agent(model, tools)

# 4. Ask the agent a question requiring the tool
inputs = {"messages": [("user", "What is the weather in Pune right now?")]]}
for chunk in agent_executor.stream(inputs, stream_mode="values"):
    chunk["messages"][-1].pretty_print()