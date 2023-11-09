from data import DataProvider
from application import QuizApplication

data_provider = DataProvider()
quiz_app = QuizApplication(data_provider)

# only print the greeting if this file is executed directly
tema = "Aeronáutica"
question = quiz_app.get_random_questions(tema)
for q in question:
    print(q)
