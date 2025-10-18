# ☁️ Azure SDK – Quick Reference

The Azure SDK provides Python libraries to securely connect and interact with Azure services like 
- OpenAI
- Cognitive Search
- Storage — essential for building AI and RAG applications.

## 🔑 Why It’s Useful

- 🔐 Authentication – Secure access via DefaultAzureCredential or API keys.
- ⚙️ Service Integration – Connects Azure OpenAI, Search, and Storage in code.
- 🧩 Resource Management – Create, update, and manage Azure resources programmatically.
- 📊 AI Workflows – Power RAG pipelines and data-driven AI apps.

## 💻 Basic Usage

1️⃣ Authenticate
```python
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()
```

2️⃣ Connect to Azure OpenAI
```python
from azure.ai.openai import AzureOpenAI
client = AzureOpenAI(credential=credential, endpoint="https://<resource>.openai.azure.com/")
```

3️⃣ Call the Model
```python
resp = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Summarize Azure SDK"}]
)
print(resp.choices[0].message["content"])
```
