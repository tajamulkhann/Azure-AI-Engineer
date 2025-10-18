# 🚀 Azure Generative AI + RAG (Retrieval-Augmented Generation)

## 🔹 Overview

This repository demonstrates building a Retrieval-Augmented Generation (RAG) system on Azure.
It combines Azure OpenAI Service for LLM generation with Azure Cognitive Search for semantic retrieval.
RAG allows LLMs to answer queries using external knowledge instead of relying solely on pre-trained knowledge.

---

## 🔹 Prerequisites for RAG with Azure AI

### 1️⃣ Azure Resources
- Storage Account → store documents.
- Embedding Deployment → Azure OpenAI deployment for embeddings.
- Chat Deployment → Azure OpenAI deployment for generation.
- Azure AI Search → semantic search over your documents.
  
### 2️⃣ Using Chat Deployment
- Upload documents to storage.
- Ingestion → Preprocessing → Indexing into Azure AI Search.

> Example services and datastore naming conventions:  
- `acasdatastore` → Azure data storage  
- `embeddingacasrag` → Embedding deployment  
- `chatmodelrag` → Chat model deployment  
- `azureaisearchrag` → Search index/service  

---

## 🔹 Workflow

### Step 1: Data Ingestion
- Load PDFs, CSVs, text files, etc.  
- Split into smaller chunks (paragraph → sentence → word) using `RecursiveCharacterTextSplitter`.

```python
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = PyPDFLoader("syllabus.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)
```

### Step 2: Embedding & Storage
- Convert text chunks into vector embeddings using Azure OpenAI.
- Store vectors in Azure AI Search.

#### Index Types
| Index Type | Description | Use Case |
|------------|-------------|----------|
| **Flat**   | Linear scan | Small datasets, exact search |
| **HNSW**   | Graph-based approximate search | Large datasets, fast search |
| **IVF**    | Clustering + inverted file | Very large datasets |
---

### Step 3: Azure OpenAI Client Setup
```python
from azure.ai.openai import OpenAIClient
from azure.core.credentials import AzureKeyCredential

client = OpenAIClient(
    endpoint="https://<your-resource>.openai.azure.com/",
    credential=AzureKeyCredential("<your-api-key>")
)

response = client.chat_completions.create(
    deployment_name="<your-chat-deployment>",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain Azure AI Search."}
    ]
)
print(response.choices[0].message.content)
```

### Step 4: Retrieval with AzureAISearchRetriever

Use LangChain’s Azure AI Search retriever instead of writing a custom function:

```python
from langchain.vectorstores import AzureAIsearch
from langchain.chat_models import AzureChatOpenAI
from langchain.chains import RetrievalQA

# Initialize retriever
retriever = AzureAIsearch(
    search_service="azureaisearchrag",
    index_name="your-index",
    api_key="<your-search-api-key>",
    embedding_function=embedding_function,  # Azure OpenAI embedding client
    top_k=5
)

# Initialize Azure OpenAI Chat model
chat_model = AzureChatOpenAI(
    deployment_name="chatmodelrag",
    openai_api_key="<your-api-key>",
    temperature=0,
    model_name="gpt-4o"
)

# Combine retrieval + generation
qa_chain = RetrievalQA.from_chain_type(
    llm=chat_model,
    retriever=retriever,
    chain_type="stuff"  # combine retrieved docs as context
)

# Ask a question
query = "Explain Azure AI Search"
answer = qa_chain.run(query)
print(answer)
```

### Process:
<img width="1934" height="910" alt="image" src="https://github.com/tajamulkhann/Azure-AI-Engineer/blob/main/Azure%20Generative%20AI/d.%20Azure%20AI%20%2B%20RAG/Working%20of%20Azure%20AI%20%2B%20RAG.png" />

- Retriever: Fetch relevant vectors/documents from search.
- Format Docs: Prepare retrieved docs as context.
- Prompt: Combine query + context for LLM.
- Model: Azure OpenAI generates context-aware response.
- Output Parser: Return clean string output.

✅ Key Benefits:

- Retrieval logic is fully handled by AzureAISearchRetriever.
- No need to manually handle embeddings or search calls.
- Easily swap or scale LLMs and AI Search indexes.
- Modular and production-ready.

🔹 Key Takeaways

- Azure OpenAI + Azure AI Search enables semantic search + intelligent generation.
- Use embeddings for accurate retrieval.
- top_k controls number of retrieved documents.
- AzureAISearchRetriever simplifies RAG pipelines.
- Fully modular: add new documents or change model deployments easily.
