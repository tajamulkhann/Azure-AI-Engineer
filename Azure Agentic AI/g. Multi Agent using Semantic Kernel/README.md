🧠 Project Goal

Automate and optimize social media posts using Azure OpenAI & Semantic Kernel multi-agent orchestration.

⚙️ Pseudo-code in Steps

1️⃣ Import Libraries

Load semantic_kernel, asyncio, and dotenv for AI orchestration and environment setup.

2️⃣ Load Environment Variables

Load Azure credentials (API_KEY, ENDPOINT, DEPLOYMENT_NAME, API_VERSION) from .env.

3️⃣ Test Azure OpenAI Connection

Initialize AzureChatCompletion and check if the model is accessible.

4️⃣ Define Multiple Agents

Analyzer Agent: Reviews tone, engagement, and target audience.

Optimizer Agent: Rewrites the post for better engagement (adds hashtags, emojis).

Reviewer Agent: Final grammar and style polishing.

5️⃣ Create Orchestration

Use SequentialOrchestration to run agents step-by-step — output of one becomes input to the next.

6️⃣ Set up Runtime

Initialize InProcessRuntime() to execute agents.

7️⃣ Pass a Business Post

Input a sample post → sent through the pipeline of agents sequentially.

8️⃣ Collect and Print Final Optimized Output

Get the final post after all three agents refine it.

9️⃣ Handle Errors and Stop Runtime

Ensure graceful shutdown and error handling.

🧩 In one line:

“It’s a multi-agent AI workflow using Semantic Kernel where each agent (Analyzer → Optimizer → Reviewer) collaboratively enhances a social media post using Azure OpenAI.”