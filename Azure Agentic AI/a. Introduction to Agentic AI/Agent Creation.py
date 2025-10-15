#Library is azure.ai.projects
# Class is AIProjectClient
# Object is project_client
# properties are agents, threads, messages, runs
# methods are create_agent, create_thread, create_message, create_and_process, list_messages, delete_agent
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

# Set your Azure AI Foundry project endpoint
project_endpoint = "https://az-agent-foundry-ga.services.ai.azure.com/api/projects/az-agent-project"

# Create AIProjectClient
project_client = AIProjectClient(
    endpoint=project_endpoint,
    credential=DefaultAzureCredential(),
)

# Use the client inside the 'with' block for all operations
with project_client:
    # Create an agent
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are a helpful agent",
    )
    print(f"Created agent, ID: {agent.id}")

    # Create a thread
    thread = project_client.agents.threads.create()
    print(f"Created thread, ID: {thread.id}")

    # Add a user message to the thread
    message = project_client.agents.messages.create(
        thread_id=thread.id,
        role="user",
        content="Who is PM of India?",
    )
    print(f"Created message, ID: {message['id']}")

    # Run the agent
    run = project_client.agents.runs.create_and_process(thread_id=thread.id, agent_id=agent.id)
    print(f"Run finished with status: {run.status}")

    if run.status == "failed":
        print(f"Run failed: {run.last_error}")

    # Retrieve and print messages
    messages = project_client.agents.messages.list(thread_id=thread.id)
    for msg in messages:
        if msg.text_messages:
            last_text = msg.text_messages[-1]
            print(f"{msg.role}: {last_text.text.value}")
    # Delete the agent
    project_client.agents.delete_agent(agent.id)
    print("Deleted agent")
