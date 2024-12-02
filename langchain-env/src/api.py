import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.qa_system import ask_question
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

origins = [
    "http://localhost:3000"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow these origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

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