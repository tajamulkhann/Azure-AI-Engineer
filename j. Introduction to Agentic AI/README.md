## Azure Agentic AI – Quick Reference

Azure Agentic AI is a framework for building autonomous AI systems that can make decisions, interact with APIs, and perform multi-step tasks with minimal human intervention.

### 1️⃣ Key Concepts
| Term               | Description                                                                                     |
| ------------------ | ----------------------------------------------------------------------------------------------- |
| **Non-Agentic AI** | Standard AI like ChatGPT — responds to prompts but doesn’t act autonomously.                    |
| **Assistant AI**   | AI that can follow structured prompts, access tools, but requires user guidance.                |
| **Agentic AI**     | Fully autonomous AI that can plan, execute actions, call APIs, and interact with external data. |

### 2️⃣ Important Components
| Component                      | Purpose                                                                            |
| ------------------------------ | ---------------------------------------------------------------------------------- |
| **Agent**                      | Core decision-making entity that plans actions based on goals.                     |
| **Skill/Plugin**               | Predefined capabilities the agent can call, e.g., translation, database query.     |
| **Function Calls**             | Enables agent to interact with APIs, fetch or modify data.                         |
| **Code Interpreter**           | Executes Python/other code for computations, data analysis, or generating outputs. |
| **BYOD (Bring Your Own Data)** | Connect your own datasets for the agent to analyze or make decisions.              |
| **WoData / Workflows**         | Structured pipelines for automating multi-step tasks.                              |

### 3️⃣ Key Functionalities

Autonomous Decision Making: Can choose which tools or APIs to use to achieve a goal.

API Orchestration: Calls external APIs automatically based on user-defined objectives.

Data Integration: Can pull in external data (BYOD) or from internal sources (WoData).

Code Execution: Handles dynamic calculations and analytics using a code interpreter.

Task Automation: Executes multi-step workflows autonomously.

### 4️⃣ Example Use Cases

Customer Support: Agent answers queries, retrieves account data, and updates records automatically.

Data Analysis: Pulls data, runs computations, generates visualizations, and summarizes insights.

Marketing Automation: Plans campaigns, sends emails, updates dashboards without human intervention.

Finance Operations: Monitors transactions, detects anomalies, triggers alerts, and prepares reports.

### Pseudo Code
```# Initialize agent
agent = AgenticAI(goal="Generate weekly sales report")

# Add skills
agent.add_skill("fetch_sales_data")
agent.add_skill("analyze_trends")
agent.add_skill("create_visualization")

# Bring your own dataset
agent.connect_data("my_sales_data.csv")

# Execute workflow
report = agent.run_workflow()

# Send report via email
agent.function_call("send_email", to="manager@example.com", attachment=report)```

### 6️⃣ Pro Tips

- Always define clear goals for your agent.

- Use BYOD for domain-specific insights.

- Monitor logs to understand decision-making paths.

- Combine Code Interpreter + Function Calls for advanced automation.

