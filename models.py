class Pergunta:
    def __init__(self, question_id, theme, difficulty, score, question, options, explanation):
        self.question_id = question_id
        self.theme = theme
        self.difficulty = difficulty
        self.score = score
        self.question = question
        self.options = [Opcao(option_data['Value'], option_data['IsCorrect']) for option_data in options]
        self.explanation = explanation

        # colocar aqui o código para criar instâncias da classe Opcao

    def __repr__(self):
        return f"<Pergunta> ID:{self.question_id}, Tema:{self.theme}, Pergunta:{self.question}"


class Opcao:
    def __init__(self, value, is_correct):
        self.value = value
        self.is_correct = is_correct

# class response
class Resposta:
     def __init__(self, question_id, option):
        self.question_id = question_id
        self.option = option

# class Pontuacao
class Pontuacao:
    def __init__(self, score, correct_answers):
        self.score = score
        self.correct_answers = correct_answers
