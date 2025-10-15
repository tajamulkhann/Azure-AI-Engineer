## Agentic AI Process

- First, we install the Azure SDK.

- Then, we install libraries like azure-ai-projects and azure-identity.

- Next, we use the Azure project endpoint.

- In the AI project, we initialize AIProjectClient(endpoint, credential).

- Optionally, we can add tools or function calls (let’s say xyz) for extra capabilities.

- Then, we set up the agent with model, instructions, and optional tools = xyz.

- After that, we create a thread for the conversation.

- Finally, we send messages, which are stored in the thread for a looped conversation.