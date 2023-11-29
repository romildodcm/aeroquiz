from fastapi import FastAPI, HTTPException, Depends, Query, Body
from fastapi.middleware.cors import CORSMiddleware
from data import DataProvider
from application import QuizApplication

app = FastAPI()
data_provider = DataProvider()
quiz_app = QuizApplication(data_provider)

# Configurar o CORS para aceitar qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir qualquer origem
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

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
    if not user_answers:
        raise HTTPException(status_code=400, detail="Empty list of answers")

    return quiz_app.validate_answers(user_answers)


