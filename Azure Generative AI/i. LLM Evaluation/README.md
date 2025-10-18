## 🧠 LLM Evaluation Metrics

| **Category**                  | **Metric**                     | **Description**                                                                                         | **Purpose**                                              |
| ----------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **1️⃣ Retriever Performance** | **Hit Rate**                   | Checks if at least one retrieved document contains the *ground-truth (gold answer)*.                    | Ensures retriever returns relevant context.              |
|                               | **MRR (Mean Reciprocal Rank)** | Measures how high the *first relevant document* appears in the ranking. (Higher = Better)               | Evaluates ranking quality of retrieved docs.             |
|                               | **Context Precision/Recall**   | Precision: % of retrieved docs that are relevant.<br>Recall: % of relevant docs successfully retrieved. | Checks retriever’s ability to surface the right context. |
| **2️⃣ Generator Performance** | **Answer Relevancy**           | Measures if the generated answer actually addresses the query. (LLM-as-judge / semantic similarity)     | Tests how relevant and on-topic the model’s response is. |
|                               | **Faithfulness**               | Checks if the generated answer is *grounded in retrieved documents* (no hallucinations).                | Ensures the model uses the retrieved context properly.   |

## 💡 Summary:
Retriever metrics measure context quality, while generator metrics measure answer quality.
Together, they ensure your RAG pipeline retrieves the right context and generates faithful, relevant answers.
