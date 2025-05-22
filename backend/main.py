from fastapi import FastAPI, Request
from pydantic import BaseModel
from .prompt_engineering import casual_prompt, formal_prompt
from .database import SessionLocal, Prompt, init_db
import subprocess

app = FastAPI()
init_db()

class QueryInput(BaseModel):
    user_id: str
    query: str

@app.post("/generate")
def generate(input_data: QueryInput):
    casual_input = casual_prompt(input_data.query)
    formal_input = formal_prompt(input_data.query)

    # Use Ollama's Mistral
    def call_ollama(prompt: str):
        result = subprocess.run(
            ["ollama", "run", "mistral", prompt],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()

    casual_response = call_ollama(casual_input)
    formal_response = call_ollama(formal_input)

    # Save to DB
    db = SessionLocal()
    record = Prompt(
        user_id=input_data.user_id,
        query=input_data.query,
        casual_response=casual_response,
        formal_response=formal_response
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    db.close()

    return {
        "casual_response": casual_response,
        "formal_response": formal_response
    }

@app.get("/history")
def get_history(user_id: str):
    db = SessionLocal()
    records = db.query(Prompt).filter(Prompt.user_id == user_id).order_by(Prompt.created_at.desc()).all()
    db.close()
    return [
        {
            "query": r.query,
            "casual_response": r.casual_response,
            "formal_response": r.formal_response,
            "created_at": r.created_at
        } for r in records
    ]
