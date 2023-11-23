from fastapi import FastAPI, HTTPException, Depends, Query, Body
from data import DataProvider
from models import Resposta
from application import QuizApplication

app = FastAPI()
data_provider = DataProvider()
quiz_app = QuizApplication(data_provider)

@app.get("/")
async def root():
 return {"greeting":"Hello world"}

@app.get("/perguntas")
async def get_questions(theme: str = Query(..., description="Theme of the questions"),
                        quantity: int = Query(6, description="Number of questions")):

    questions = quiz_app.get_random_questions(theme, quantity)
    return questions

@app.post("/validar-respostas")
async def validate_answers(user_answers: list = Body(...)):
    # se a lsita for vaiza, retorna erro bad request
    if not user_answers:
        raise HTTPException(status_code=400, detail="Empty list of answers")

    # total_score, correct_answers =
    return quiz_app.validate_answers(user_answers)


