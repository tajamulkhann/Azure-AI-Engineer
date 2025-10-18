## 🧠 LLM Evaluation Metrics

| **Category**                  | **Metric**                     | **Description**                                                                                         | **Purpose**                                              |
| ----------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **1️⃣ Retriever Performance** | **Hit Rate**                   | Checks if at least one retrieved document contains the *ground-truth (gold answer)*.                    | Ensures retriever returns relevant context.              |
|                               | **MRR (Mean Reciprocal Rank)** | Measures how high the *first relevant document* appears in the ranking. (Higher = Better)               | Evaluates ranking quality of retrieved docs.             |
|                               | **Context Precision/Recall**   | Precision: % of retrieved docs that are relevant.<br>Recall: % of relevant docs successfully retrieved. | Checks retriever’s ability to surface the right context. |
| **2️⃣ Generator Performance** | **Answer Relevancy**           | Measures if the generated answer actually addresses the query. (LLM-as-judge / semantic similarity)     | Tests how relevant and on-topic the model’s response is. |
|                               | **Faithfulness**               | Checks if the generated answer is *grounded in retrieved documents* (no hallucinations).                | Ensures the model uses the retrieved context properly.   |

## Code
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

## 💡 Summary:
| Stage     | Metric                           | Evaluated By                                    | Tool / Method                  |
| --------- | -------------------------------- | ----------------------------------------------- | ------------------------------ |
| Retriever | Hit Rate, MRR, Precision, Recall | Matching retrieved docs vs gold                 | Ragas / Custom                 |
| Generator | Answer Relevancy, Faithfulness   | Comparing generated vs gold / retrieved context | Ragas / TruLens / LLM-as-Judge |

