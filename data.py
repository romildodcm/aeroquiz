import json
from models import Quiz

class QuizData:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if QuizData.__instance == None:
            QuizData()
        return QuizData.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if QuizData.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            QuizData.__instance = self
            with open('data.json') as f:
                data = json.load(f)
                self.quiz = Quiz(data['title'], data['questions'])

    def get_quiz(self):
        return self.quiz
