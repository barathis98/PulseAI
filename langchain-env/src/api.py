import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.qa_system import ask_question



app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask(request: QuestionRequest):
    question = request.question
    print(question)


    try:
        answer = ask_question(question)
        return {"question": question,"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to answer question: {e}")