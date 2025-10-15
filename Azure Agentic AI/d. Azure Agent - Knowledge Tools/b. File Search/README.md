1) Set up Azure credentials (tenant ID, client ID, secret) and project connection.
2) Initialize Azure AI Project client with authentication.
3) Upload a PDF file (gpt-4-system-card.pdf) to Azure for processing.
4) Create a vector store from the uploaded file for semantic search.
5) Create a FileSearchTool connected to the vector store.
6) Create an agent with GPT-4o-mini model and attach the file search tool.
7) Create a conversation thread for the session.
8) Start interactive loop:
   - Get user question (e.g., "main points in the file")
   - Upload file as message attachment for context
   - Send user message to the thread
   - Run the agent (it searches the vector store for relevant content)
   - Agent returns response with citations from the uploaded document
   - Display the grounded response to user
   - Continue until user types "end"
9) Clean up by deleting vector store and agent.
