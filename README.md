# 🤖 HR AI Assistance

## Description

HR AI Assistance is an AI-powered recruitment assistant built using **LangChain**, **Ollama**, and **FAISS** to automate common HR tasks. The application leverages Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and custom tools to assist recruiters with candidate screening, interview preparation, and company policy queries.

The assistant can retrieve information from company HR documents, determine candidate eligibility based on required skills, calculate work experience, generate interview questions, and extract structured information from resumes.

---

## ✨ Features

- 📄 Resume Information Extraction
- 🧑‍💼 Candidate Eligibility Checker
- 📅 Experience Calculator
- 🎯 AI-Generated Interview Questions
- 📚 Company Policy Question Answering using RAG
- 🔍 FAISS Vector Search
- 🤖 Tool Calling Agent with LangChain
- 📝 Structured Output using Pydantic

---

## 🛠️ Tech Stack

### AI Framework
- LangChain
- LangChain Community
- LangGraph (optional for future workflow enhancements)

### Large Language Model
- Ollama
- Qwen3:4B

### Embeddings
- Nomic Embed Text (`nomic-embed-text`)

### Retrieval-Augmented Generation (RAG)
- FAISS Vector Database

### Backend
- Python

### Data Validation
- Pydantic

### Development Tools
- Visual Studio Code
- Git
- GitHub

---

## 📁 Project Structure

```
HR-AI-Assistance/
│
├── documents/          # HR policy documents
├── hr_vector_db/       # Generated FAISS vector database (ignored in Git)
├── hr_agent.py         # Main AI HR assistant
├── vector_db.py        # Creates the FAISS vector database
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ How It Works

1. HR policy documents are loaded and converted into vector embeddings.
2. FAISS stores the embeddings for efficient semantic search.
3. The AI agent uses tool calling to:
   - Calculate candidate experience
   - Check candidate eligibility
   - Generate interview questions
   - Retrieve company policies using RAG
4. Resume text can be parsed into structured candidate information using Pydantic.

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/your-username/HR-AI-Assistance.git
cd HR-AI-Assistance
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Step 1: Generate the Vector Database

```bash
python vector_db.py
```

### Step 2: Run the HR Assistant

```bash
python hr_agent.py
```

Type `exit` to end the session.

To extract candidate details from a resume, use:

```text
resume: <Paste resume text here>
```

---

## 📌 Example Queries

- What is the company's leave policy?
- What is the notice period?
- Generate Python interview questions.
- Is a candidate with Python, SQL, and Git eligible?
- Calculate experience for someone who started in 2020.
- Extract details from a resume.

---

## 🔮 Future Improvements

- Web-based user interface
- Chat history using SQLite
- Support for PDF and DOCX resume parsing
- Multi-user authentication
- Human-in-the-loop approval workflow
- Integration with HRMS platforms
- Email notifications for recruiters

---

## 👨‍💻 Author

**Ananth**

---
