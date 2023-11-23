from data import DataProvider
from application import QuizApplication

data_provider = DataProvider()
quiz_app = QuizApplication(data_provider)

# only print the greeting if this file is executed directly
tema = "Aeronáutica"
# question = quiz_app.get_random_questions(tema)
# for q in question:
#     print(q)

total = quiz_app.validate_answers([{'question_id': 1, 'option': 'A'}, {'question_id': 2, 'option': 'Neil Armstrong'}])
print(total.score)
print(total.correct_answers)
