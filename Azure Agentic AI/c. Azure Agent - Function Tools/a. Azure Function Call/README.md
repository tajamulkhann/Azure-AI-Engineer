1) Initialize credentials and connect to the Azure AI project.
2) Define a weather_lookup tool (inputs: location, datetime; output: temp/conditions).
3) Create an agent with instructions and register the tool.
4) Start a new conversation thread.
5) Add the user’s message (e.g., “Weather in Bangalore tomorrow morning?”).
6) Run the agent on the thread.
7) If the agent requests a tool call:
     - Parse arguments
     - Call weather_lookup
     - Send tool output back to the agent
8) Wait for completion and get the assistant’s final message.
9) Print the answer and delete the agent to clean up.
