## 🧠 Project Goal

Automate and optimize social media posts using Azure OpenAI & Semantic Kernel multi-agent orchestration.

| Step                             | Description                                              | Pseudo-code                                                |
| -------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------- |
| 1️⃣ Import Libraries             | Load AI orchestration & environment tools                | `import semantic_kernel, asyncio, dotenv`                  |
| 2️⃣ Load Environment Variables   | Load Azure credentials                                   | `dotenv.load_dotenv(); API_KEY=...; ENDPOINT=...`          |
| 3️⃣ Test Azure OpenAI Connection | Check model availability                                 | `client = AzureChatCompletion(...); client.test()`         |
| 4️⃣ Define Multiple Agents       | Create agents for analysis, optimization, and review     | `AnalyzerAgent`, `OptimizerAgent`, `ReviewerAgent`         |
| 5️⃣ Create Orchestration         | Run agents sequentially, passing output from one to next | `SequentialOrchestration([Analyzer, Optimizer, Reviewer])` |
| 6️⃣ Set up Runtime               | Initialize execution environment                         | `runtime = InProcessRuntime()`                             |
| 7️⃣ Pass a Business Post         | Input sample post into agent pipeline                    | `output = runtime.run(post)`                               |
| 8️⃣ Collect Final Output         | Get refined post after all agents                        | `print(final_post)`                                        |
| 9️⃣ Handle Errors                | Ensure graceful shutdown                                 | `try: ... except: runtime.stop()`                          |

### Summary (One Line)

A multi-agent AI workflow using Semantic Kernel where each agent (Analyzer → Optimizer → Reviewer) collaboratively enhances a social media post using Azure OpenAI.
