## 🤖 Azure Agentic AI – Quick Reference

Azure Agentic AI (part of Azure AI Foundry – Agent Service) lets you build autonomous agents that can reason, call tools (functions/APIs), and use knowledge from your own data to produce intelligent, grounded answers.

### 1️⃣ Setup & Authentication
```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Authenticate and connect to Azure AI Project
credential = DefaultAzureCredential()
project_client = AIProjectClient(endpoint="https://<your-project>.projects.azure.com", credential=credential)
```

### 2️⃣ Define a Tool (Function Call Example)
```python
# Define a custom function that the agent can call
def weather_lookup(location: str, datetime: str):
    return {"temp": "28°C", "condition": "Sunny"}

toolset = [
    {
        "name": "weather_lookup",
        "description": "Get weather details for a given location and time",
        "inputs": {"location": "string", "datetime": "string"},
        "function": weather_lookup
    }
]
```

### 3️⃣ Create and Configure an Agent
```python
agent = project_client.agents.create_agent(
    model="gpt-4o-mini",
    name="weather-agent",
    instructions="You are a helpful agent that provides weather information using real-time data.",
    toolset=toolset
)
```

### 4️⃣ Run a Conversation
```python
# Start a conversation thread
thread = project_client.agents.create_thread(agent.id)
project_client.agents.add_user_message(thread.id, "Weather in Bangalore tomorrow morning?")

# Run the agent
run = project_client.agents.run(agent.id, thread.id)
project_client.agents.wait_for_completion(run.id)

# Fetch and print the final response
response = project_client.agents.get_response(thread.id)
print(response)
```

### 5️⃣ Knowledge (BYOD) Integration
You can attach knowledge sources (e.g., documents, Azure Cognitive Search index, or custom datasets):
```python
knowledge = project_client.knowledge_sources.upload_files(["weather_data.pdf"])
agent = project_client.agents.create_agent(
    model="gpt-4o-mini",
    name="weather-knowledge-agent",
    instructions="Use the uploaded document to answer weather-related questions.",
    knowledge_sources=[knowledge]
)
```

### Summary
| Step                       | Purpose                                                 | Key Code / Action                                                         |
| -------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------- |
| 1️⃣ Setup & Authentication | Connect to Azure AI Project                             | `DefaultAzureCredential()` + `AIProjectClient(endpoint, credential)`      |
| 2️⃣ Define Tools           | Create functions the agent can call                     | Define Python function + wrap in `toolset` with name, description, inputs |
| 3️⃣ Create Agent           | Configure the agent with model, instructions, and tools | `project_client.agents.create_agent(model, name, instructions, toolset)`  |
| 4️⃣ Run Conversation       | Start interaction & get responses                       | `create_thread()`, `add_user_message()`, `run()`, `get_response()`        |
| 5️⃣ Knowledge Integration  | Attach documents or data for grounded answers           | `upload_files()` + `knowledge_sources=[...]` in agent creation            |
| 6️⃣ Cleanup                | Delete agents when done                                 | `project_client.agents.delete(agent.id)`                                  |

