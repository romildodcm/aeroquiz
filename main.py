from fastapi import FastAPI, HTTPException, Depends
from data import DataProvider
from application import QuizApplication

app = FastAPI()
data_provider = DataProvider()
quiz_app = QuizApplication(data_provider)

@app.get("/")
async def root():
 return {"greeting":"Hello world"}

@app.get("/perguntas/{theme}")
async def get_questions(theme: str):
    questions = quiz_app.get_random_questions(theme)
    return questions

@app.post("/validar-respostas")
async def validate_answers(user_answers: list):
    total_score, correct_answers = quiz_app.validate_answers(user_answers)
    return {"score": total_score, "correct_answers": correct_answers}


