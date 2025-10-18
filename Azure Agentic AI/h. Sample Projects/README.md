# 🚀 Multi-Agent Social Media Post Optimizer

**Description:** Automates and enhances social media posts using **Azure OpenAI** and **Semantic Kernel**.  
Three sequential agents (Analyzer → Optimizer → Reviewer) analyze, improve, and finalize posts for maximum engagement.

✅ Key Points to Explain in an Interview:

- Agents: Analyzer → Optimizer → Reviewer
- Flow: SequentialOrchestration passes output from one agent to the next.
- Runtime: InProcessRuntime executes the pipeline asynchronously.
- Connection: AzureChatCompletion links agents to Azure OpenAI model.
- Callback: show_response prints each agent’s output for debugging.

```python
# ✅ Simple Multi-Agent Social Media Post Optimizer using Azure OpenAI & Semantic Kernel

import os, asyncio
from dotenv import load_dotenv
from semantic_kernel.agents import ChatCompletionAgent, SequentialOrchestration
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.agents.runtime import InProcessRuntime
from semantic_kernel.contents import ChatMessageContent

# Load Azure credentials
load_dotenv()
AZURE_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

# Test connection
async def test_connection():
    try:
        AzureChatCompletion(
            api_key=AZURE_KEY, endpoint=AZURE_ENDPOINT,
            deployment_name=AZURE_DEPLOYMENT, api_version=AZURE_VERSION
        )
        print("✅ Azure OpenAI connection successful!")
        return True
    except:
        print("❌ Connection failed. Check credentials!")
        return False

# Define agents
def get_agents():
    service = AzureChatCompletion(
        api_key=AZURE_KEY, endpoint=AZURE_ENDPOINT,
        deployment_name=AZURE_DEPLOYMENT, api_version=AZURE_VERSION
    )

    analyzer = ChatCompletionAgent(
        "AnalyzerAgent",
        instructions="Analyze the post for tone, engagement, and audience.",
        service=service
    )
    optimizer = ChatCompletionAgent(
        "OptimizerAgent",
        instructions="Improve post engagement: hashtags, emojis, CTA.",
        service=service
    )
    reviewer = ChatCompletionAgent(
        "ReviewerAgent",
        instructions="Finalize post: grammar, hashtags, emojis, CTA.",
        service=service
    )
    return [analyzer, optimizer, reviewer]

# Callback to print agent responses
def show_response(message: ChatMessageContent):
    print(f"\n--- {message.name} ---\n{message.content}\n")

# Run multi-agent orchestration
async def run_post(post: str):
    agents = get_agents()
    orchestration = SequentialOrchestration(agents, agent_response_callback=show_response)
    runtime = InProcessRuntime()
    runtime.start()
    try:
        result = await orchestration.invoke(task=post, runtime=runtime)
        final_post = await result.get(timeout=60)
        print("🎉 FINAL POST:\n", final_post)
    finally:
        await runtime.stop_when_idle()

# Main
async def main():
    if not AZURE_KEY:
        print("❌ Set Azure OpenAI credentials first!"); return
    if not await test_connection(): return

    sample_post = """
    Hi folks, launching a new Beginners to Pro AI course on Udemy covering AI Frameworks and Models.
    """
    print("📝 Original Post:\n", sample_post)
    await run_post(sample_post)

if __name__ == "__main__":
    asyncio.run(main())
```