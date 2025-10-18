# 🧠 Freshdesk Agent App with Azure Agentic AI

**Description:**  
Automates customer support in Freshdesk using Azure Agentic AI. Classifies tickets, generates intelligent responses, and prioritizes workflow.

---

## 🚀 Features
- Automatic ticket classification
- Context-aware response generation
- Ticket prioritization
- Easy Freshdesk API integration

---

## ⚙️ Prerequisites
- Azure subscription with OpenAI access
- Freshdesk account with API access
- Python 3.8+
- Required Python packages (`pip install -r requirements.txt`)

---

## 📦 Installation
```bash
git clone https://github.com/tajamulkhann/Azure-AI-Engineer.git
cd Azure-AI-Engineer/Azure\ Agentic\ AI/e.\ Fresh\ Desk\ Agent\ App
pip install -r requirements.txt
```

## Set environment variables in .env:
```python
AZURE_OPENAI_API_KEY=your_key
AZURE_OPENAI_ENDPOINT=your_endpoint
FRESHDESK_API_KEY=your_key
FRESHDESK_DOMAIN=your_domain
```
## Usage
python app.py

## 🔄 Workflow

- Fetch tickets from Freshdesk
- Analyze & generate response using Azure AI
- Update ticket with response and classification
