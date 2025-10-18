# 🚀 Azure Generative AI + RAG (Retrieval-Augmented Generation)

## 🔹 Overview

This repository demonstrates building a Retrieval-Augmented Generation (RAG) system on Azure.
It combines Azure OpenAI Service for LLM generation with Azure Cognitive Search for semantic retrieval.
RAG allows LLMs to answer queries using external knowledge instead of relying solely on pre-trained knowledge.

---

## 🔹 Prerequisites for RAG with Azure AI

### Azure Resources & Libraries
- Storage Account → store documents.
- Embedding Deployment → Azure OpenAI deployment for embeddings.
- Chat Deployment → Azure OpenAI deployment for generation.
- Azure AI Search → semantic search over your documents.
  
```python
from langchain.vectorstores import AzureAIsearch
from langchain.chat_models import AzureChatOpenAI
from langchain.chains import RetrievalQA
```

### 1️⃣ Load documents from storage (e.g., PDF, text, CSV)
```python
loader = PyPDFLoader("syllabus.pdf")
docs = loader.load()  # docs is a list of Document objects
```

### 2️⃣ Split documents into smaller chunks for embedding
```python
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)  # manageable chunks for embedding
```

### 3️⃣ Generate embeddings for each chunk using Azure OpenAI embedding deployment
```python
# Define your embedding function (Azure OpenAI)
from langchain.embeddings import OpenAIEmbeddings

embedding_function = OpenAIEmbeddings(
    deployment="embeddingacasrag",  # your Azure OpenAI embedding deployment name
    model="text-embedding-3-large",  # Azure OpenAI embedding model
    chunk_size=1
)
```
### 4️⃣ Push chunks + embeddings into Azure AI Search index

#### Index Types
| Index Type | Description | Use Case |
|------------|-------------|----------|
| **Flat**   | Linear scan | Small datasets, exact search |
| **HNSW**   | Graph-based approximate search | Large datasets, fast search |
| **IVF**    | Clustering + inverted file | Very large datasets |
---

```python
# Initialize Azure AI Search vector store
vector_store = AzureAIsearch(
    search_service="azureaisearchrag",  # your Azure AI Search service name
    index_name="your-index",             # AI Search index name
    api_key="<your-search-api-key>",     # Azure AI Search API key
    embedding_function=embedding_function,
    top_k=5                               # default top-k for retrieval
)

# Add documents to Azure AI Search (creates embeddings internally)
vector_store.add_documents(chunks)
```

### 5️⃣ Initialize retriever (fetch relevant documents from AI Search)
```python
retriever = vector_store.as_retriever(top_k=5)
```

### 5️⃣ Initialize Azure OpenAI Chat model for generation
```python
chat_model = AzureChatOpenAI(
    deployment_name="chatmodelrag",  # Azure OpenAI chat deployment
    openai_api_key="<your-api-key>",
    temperature=0,
    model_name="gpt-4o"
)
```

### 7️⃣ Combine retriever + chat model into RAG pipeline
```python
qa_chain = RetrievalQA.from_chain_type(
    llm=chat_model,
    retriever=retriever,
    chain_type="stuff"  # "stuff" combines all retrieved docs as context
)
```

### Step 8️⃣: Ask a question and get answer
```python
query = "Explain Azure AI Search"
answer = qa_chain.run(query)
print(answer)
```

### Step 9️⃣: Evaluate LLM Performance


| **Category**                  | **Metric**                     | **Description**                                                                                         | **Purpose**                                              |
| ----------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Retriever Performance** | **Hit Rate**                   | Checks if at least one retrieved document contains the ground-truth (gold answer).                      | Ensures retriever returns relevant context.              |
|                               | **MRR (Mean Reciprocal Rank)** | Measures how high the first relevant document appears in the ranking. (Higher = Better)                 | Evaluates ranking quality of retrieved docs.             |
|                               | **Context Precision/Recall**   | Precision: % of retrieved docs that are relevant.<br>Recall: % of relevant docs successfully retrieved. | Checks retriever’s ability to surface the right context. |
| **Generator Performance** | **Answer Relevancy**           | Measures if the generated answer actually addresses the query. *(LLM-as-judge / semantic similarity)*   | Tests how relevant and on-topic the model’s response is. |
|                               | **Faithfulness**               | Checks if the generated answer is grounded in retrieved documents *(no hallucinations).*                | Ensures the model uses the retrieved context properly.   |


```python
# Example using Ragas
from datasets import load_dataset
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision

dataset = load_dataset("my_rag_results")  # your RAG eval dataset
results = evaluate(
    dataset=dataset,
    metrics=[faithfulness, answer_relevancy, context_precision]
)
print(results)
```


### Summary
| Step | Purpose                                                    |
| ---- | ---------------------------------------------------------- |
| 1    | Load raw documents from storage                            |
| 2    | Split documents into smaller chunks for embedding          |
| 3    | Create embeddings for each chunk using Azure OpenAI        |
| 4    | Push embeddings + chunks to Azure AI Search (vector store) |
| 5    | Initialize retriever to fetch top-k relevant documents     |
| 6    | Initialize Azure OpenAI chat model                         |
| 7    | Combine retriever + chat model into a RAG QA chain         |
| 8    | Ask a query → model returns answer using retrieved context |
| 9    | Evalaute LLM + RAG Performance|
