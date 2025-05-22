#  AI Prompt Style Generator

A full-stack AI-powered prototype using prompt engineering and local LLM inference via Ollama + Mistral. The app allows users to input a question and receive two responses:

- A **casual/creative** explanation
- A **formal/analytical** explanation

All interactions are saved in a PostgreSQL database and displayed in a responsive Streamlit interface.

---

##  Features

-- Prompt engineering with two distinct response styles  
-- FastAPI microservice backend  
-- PostgreSQL database integration  
-- Local AI model execution with [Ollama](https://ollama.com) + [Mistral](https://ollama.com/library/mistral)  
-- Streamlit web UI  
-- API to fetch interaction history  
-- Ready for local development and extension

---

##  Tech Stack

| Component     | Technology            |
|---------------|------------------------|
| LLM           | Ollama (Mistral)       |
| Backend       | FastAPI                |
| Frontend      | Streamlit              |
| Database      | PostgreSQL             |
| ORM           | SQLAlchemy             |
| Environment   | Python + Dotenv        |
| Testing       | Pytest (optional)      |

---

## 🧠 Prompt Engineering Strategy

This app uses **two prompt styles** for every user query to simulate different tones and purposes:

1. **Casual Prompt**  
   Tailored for informal settings. The prompt encourages the LLM to explain as if talking to a friend.

2. **Formal Prompt**  
Designed for academic, professional, or analytical use cases.



This separation enables flexible AI usage in both relaxed and serious contexts.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/arun4589/twintone.git
cd ai_microservice_project
```
### 2.Setup Virtual Environment
```bash
yoliday/scripts/activate
```

### 3.Install dependencies

```bash
pip install -r requirements.txt
```
### 4.setup PostgreSQL
```bash
CREATE DATABASE ai_app;
```
Edit .env
```bash
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/ai_app
```
### 5.start Backend server(FastAPI)
```bash
uvicorn backend.main:app --reload
```

### 6.streamlit
```bash
streamlit run frontend/app.py
```

### Make sure to install Ollama's Mistral
```bash
ollama run mistral
```
