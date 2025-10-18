## 🧠 LLM Evaluation Metrics

### 1️⃣ Retriever Evaluation
You’re testing: Did the retriever fetch the right context documents?

| Metric                         | What it Measures                                                       | How to Evaluate Practically                                                                                                 |
| ------------------------------ | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Hit Rate**                   | Whether at least one retrieved doc contains the correct (gold) answer. | For each query: check if any of the top-k retrieved docs contain the gold answer → compute % of queries where this is true. |
| **MRR (Mean Reciprocal Rank)** | Rank position of the first relevant doc.                               | For each query: `1 / rank_of_first_relevant_doc`. Average across all queries.                                               |
| **Precision / Recall**         | How many retrieved docs are relevant vs missed.                        | Compare retrieved docs vs. gold-labeled relevant docs. Compute Precision = TP/(TP+FP), Recall = TP/(TP+FN).                 |

#### 📦 Implementation Tools:

- LangChain → langchain.evaluation module
- ragas (by HuggingFace) → built-in retriever metrics (context_precision, context_recall, mrr)
- Custom Python logic with embedding similarity (e.g., cosine similarity > threshold = relevant).

### 2️⃣ Generator Evaluation
You’re testing: Did the LLM use context correctly and produce a truthful, relevant answer?

| Metric               | What it Measures                                                                      | How to Evaluate Practically                                                                                                              |
| -------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Answer Relevancy** | How well the generated answer addresses the question.                                 | Use LLM-as-a-judge (e.g., GPT-4) or semantic similarity between generated answer and gold answer.                                        |
| **Faithfulness**     | Whether the answer’s statements are grounded in retrieved context (no hallucination). | Check if each claim in the answer can be found (or supported) in the retrieved documents. Tools like `ragas.faithfulness` automate this. |

#### 📦 Implementation Tools:

- 🤗 Ragas → faithfulness, answer_relevancy, context_precision, etc.
- 🧪 TruLens → Evaluate with trulens_eval decorators (@instrument) to log and score LLM responses.
- 🧠 LLM-as-Judge → Use a model (like GPT-4) to score each generated answer on a 1-5 scale for relevance and factuality.

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

