class Pergunta:
    def __init__(self, question_id, theme, difficulty, score, question, options, explanation):
        self.question_id = question_id
        self.theme = theme
        self.difficulty = difficulty
        self.score = score
        self.question = question
        self.options = [Opcao(option_data['Value'], option_data['IsCorrect']) for option_data in options]
        self.explanation = explanation

    def __repr__(self):
        return f"<Pergunta> ID:{self.question_id}, Tema:{self.theme}, Pergunta:{self.question}"

class Opcao:
    def __init__(self, value, is_correct):
        self.value = value
        self.is_correct = is_correct
        self.selected = False

class Resposta:
     def __init__(self, question_id, option):
        self.question_id = question_id
        self.option = option

class Pontuacao:
    def __init__(self, score, correct_answers, questions):
        self.score = score
        self.correct_answers = correct_answers
        self.questions = questions


# score
# número de respostas corretas
# todas as questões com a resposta marcada pelo usuário e a resposta correta

# Pergunta e Resposta
class ResultadoFinal:
    def __init__(self, pontuacao, questions):
        self.pontuacao = pontuacao
        self.questions = questions
