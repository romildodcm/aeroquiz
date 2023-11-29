import json
from models import Pergunta

# Factory Method para criar instâncias da classe Pergunta
def question_factory(question_data):

    return Pergunta(
        question_data['question_id'],
        question_data['theme'],
        question_data['difficulty'],
        question_data['score'],
        question_data['question'],
        question_data['options'],
        question_data['explanation']
    )

class DataProvider:
    _instance = None

    def __new__(cls):
        # Padrão de Projeto Singleton para ter apenas uma instância da classe DataProvider
        if cls._instance is None:
            cls._instance = super(DataProvider, cls).__new__(cls)
            with open('data.json', 'r') as file:
                cls._instance.data = json.load(file)
        return cls._instance

    def get_question_by_id(self, question_id):
        for question_data in self.data:
            if question_data['question_id'] == question_id:
                return question_factory(question_data)

    def get_all_questions(self):
        # Método para obter todas as questões.
        return [question_factory(question_data) for question_data in self.data]

    def get_questions_by_theme(self, theme):
        # Método para obter questões por tema.
        return [question_factory(question) for question in self.data if question['theme'] == theme]

    def get_questions_by_id_range(self, start_id, end_id):
        # Método para obter questões por um intervalo de IDs.
        return [question_factory(question_data) for question_data in self.data if start_id <= question_data['question_id'] <= end_id]
