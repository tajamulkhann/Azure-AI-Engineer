# 🚀 Azure Generative AI + RAG (Retrieval-Augmented Generation)

## 🔹 Overview
This repository demonstrates building a **Retrieval-Augmented Generation (RAG)** system on Azure.  
It combines **Azure OpenAI Service** for LLM generation with **Azure Cognitive Search** for semantic retrieval.  
RAG allows LLMs to answer queries using **external knowledge** instead of relying solely on pre-trained knowledge.

---

## 🔹 Prerequisites for RAG with Azure AI

### 1️⃣ Azure Resources
- **Storage Account**: To store your documents and data.  
- **Embedding Deployment**: Azure OpenAI deployment for generating embeddings.  
- **Chats Deployment**: Azure OpenAI deployment for chat generation.  
- **Azure AI Search Service**: Semantic search over your documents.

### 2️⃣ Using Chat Deployment
- **Upload documents** to storage.  
- **Ingestion → Preprocessing → Indexing** into Azure Cognitive Search.  

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

### Step 2: Embedding & Storage
- Convert text chunks into **vector embeddings** using Azure OpenAI or Hugging Face.  
- Store vectors in **Azure Cognitive Search** (vector DB).  

#### Index Types
| Index Type | Description | Use Case |
|------------|-------------|----------|
| **Flat**   | Linear scan | Small datasets, exact search |
| **HNSW**   | Graph-based approximate search | Large datasets, fast search |
| **IVF**    | Clustering + inverted file | Very large datasets |
| **PQ**     | Quantized vectors | Memory-efficient retrieval |

---

### Step 3: Azure OpenAI Client Setup
```python
from azure.ai.openai import OpenAIClient
from azure.core.credentials import AzureKeyCredential

# Initialize client
client = OpenAIClient(
    endpoint="https://<your-resource>.openai.azure.com/",
    credential=AzureKeyCredential("<your-api-key>"),
    api_version="2023-07-01-preview"
)

# Example usage
response = client.chat_completions.create(
    deployment_name="<your-chat-deployment>",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain Azure Cognitive Search."}
    ]
)
print(response.choices[0].message.content)
```

### Step 4: Retrieval

- User query is converted into embeddings.

- Retrieve top-k similar documents from Azure Cognitive Search index.

```python
def retrieve_top_k(query: str, k: int = 5):
    """Retrieve top-k similar documents from Azure Cognitive Search"""
    # 1️⃣ Get embedding of the query
    query_vector = get_embedding(query)

    # 2️⃣ Use vector search in Azure Cognitive Search
    results = search_client.search(
        vector=query_vector,
        top=k,
        vector_fields="embedding_vector"  # The field where your vectors are stored
    )

    # 3️⃣ Extract and return documents
    docs = [doc["content"] for doc in results]
    return docs
```

### Step 5: Augmented Generation (RAG Chain)
```python
from langchain.schema import RunnablePassthrough, StrOutputParser

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)
```

### Process:

- Retriever: Fetch relevant vectors/documents from search.
- Format Docs: Prepare retrieved docs as context.
- Prompt: Combine query + context for LLM.
- Model: Azure OpenAI generates context-aware response.
- Output Parser: Return clean string output.

### 🔹 Key Takeaways

- Azure OpenAI + Cognitive Search enables semantic search + intelligent generation.
- Embeddings are crucial for accurate retrieval.
- Index type affects speed and accuracy: HNSW recommended for large datasets.
- Use unique IDs for each document vector in the datastore.
- Fully modular: add new documents or change model deployments easily.
