from random import sample
from models import Pontuacao, Resposta, Opcao

class QuizApplication:
    def __init__(self, data_provider):
        self.data_provider = data_provider

    def adapt_questions(self, questions):
        # Função para adaptar perguntas e opções para um formato sem o campo da resposta correta.
        adapted_questions = []
        for question in questions:
            for option in question.options:
                del option.is_correct
            # adapted_options = [(option.value, option.selected) for option in question.options]
            adapted_question = {
                'question_id': question.question_id,
                'theme': question.theme,
                'difficulty': question.difficulty,
                # 'score': question.score,
                'question': question.question,
                'options': question.options,
                # 'explanation': question.explanation
            }
            adapted_questions.append(adapted_question)
        return adapted_questions

    def get_random_questions(self, theme, quantity=5):
        a = []
        questions = self.data_provider.get_questions_by_theme(theme)
        if len(questions) > quantity:
            questions = sample(questions, quantity)
        return self.adapt_questions(questions)
        # return self.adapt_questions(sample(questions, quantity))

    def validate_answers(self, user_answers):
        questoesRespostas = []
        total_score = 0
        correct_answers = 0

        for user_answer in user_answers:
            question = self.data_provider.get_question_by_id(user_answer['question_id'])

            if question:
                for option in question.options:
                    if option.is_correct and option.value == user_answer['option']:
                        total_score += question.score
                        correct_answers += 1
                        option.selected = True
                    elif option.value == user_answer['option']:
                        option.selected = True
                questoesRespostas.append(question)

        return Pontuacao(total_score, correct_answers, questoesRespostas)



        # answers = [Resposta(user_answer['question_id'], Opcao(user_answer['option'])) for user_answer in user_answers]

        # for answer in answers:
        #     question = self.data_provider.get_question_by_id(answer.question_id)
        #     if question:
        #         for option in question.options:
        #             if option.is_correct and option.value == answer.option:

        #                 total_score += question.score
        #                 correct_answers += 1

        # return Pontuacao(total_score, correct_answers)



    def get_questions_by_id_range(self, start_id, end_id):
        questions = self.data_provider.get_questions_by_id_range(start_id, end_id)
        return self.adapt_questions(questions)

    # um método que retore o resultado do formulário com a pontuação, o número de respostas corretas e todas as questões


    # sugestão do template methode no front: reexibir o formulário, mas o card da questão fica vermelho para as erradas e verde para as corretas
