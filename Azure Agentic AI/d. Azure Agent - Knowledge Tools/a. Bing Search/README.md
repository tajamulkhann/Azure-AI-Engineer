1) Set up environment variables and Azure credentials.
2) Initialize Azure AI Project client with authentication.
3) Get the Bing Search connection from Azure and create a BingGroundingTool.
4) Create an agent with GPT-4o model and register the Bing tool.
5) Create a conversation thread for the session.
6) Start interactive loop:
   - Get user input
   - Send user message to the thread
   - Run the agent (it decides whether to search Bing for current info)
   - If agent calls Bing tool, it searches the web and incorporates results
   - Display the grounded response to user
   - Continue until user types "end"
7) Clean up by deleting the agent.
