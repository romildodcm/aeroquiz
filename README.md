# aeroquiz

### Quiz sobre aeronáutica e aeroespacial

**Objetivo:** Implementar uma aplicação do tipo Quiz onde o usuário pode testar seu conhecimento em determinado assunto(s). O app lê de um arquivo ou base de dados no mínimo 10 questões e apresenta ao usuário que poderá escolher uma alternativa por questão. Ao final é apresentado o resultado do quiz (nota, total de acertos). Na primeira fase, iniciar com a definição dos itens:

**1. Modelo de dados (JSON), com as perguntas e respostas. O modelo é o próprio arquivo json, já com os dados que serão usados.**

A modelagem inicial do JSON com as perguntas é apresentada a seguir. O arquivo completo pode ser encontrado em [modelodados.json](modelodados.json).

```JSON
[
  {
    "question_id":2,
    "theme":"Aeroespacial",
    "difficulty":1,
    "score":10,
    "question":"Qual foi o primeiro ser humano a caminhar na Lua?",
    "options":[
      { "Value":"Neil Armstrong", "IsCorrect":true },
      { "Value":"Buzz Aldrin", "IsCorrect":false },
      { "Value":"Yuri Gagarin", "IsCorrect":false },
      { "Value":"John Glenn", "IsCorrect":false }
    ],
    "explanation":"Neil Armstrong foi o primeiro ser humano a caminhar na Lua durante a missão Apollo 11."
  }
]
```

**2. Definir as classes do App no python para representar os dados.**

A seguir estão as classes definidas inicialmente, durante a implementação podem ser necessárias alterações.

```python
class Question:
    def __init__(self, question_id, theme, difficulty, score, question, options, explanation):
        self.question_id = question_id
        self.theme = theme
        self.difficulty = difficulty
        self.score = score
        self.question = question
        self.options = options
        self.explanation = explanation

class Option:
    def __init__(self, value, is_correct):
        self.value = value
        self.is_correct = is_correct
```

**3. Escolher 3 padrões de projetos que serão usados durante a implementação do projeto (fase 2). Colocar o nome do padrão de projeto e para qual contexto ele seria utilizado no seu projeto (explicar brevemente).**

**Factory:** deve ser usado para centralizar a criação de objetos Question a partir do JSON, promovendo a flexibilidade para futuras adições de tipos de questões e mantendo a lógica de criação separada da lógica principal.

**Observer:** deve possibilitar o acompanhamento dinâmico do score do usuário, permitindo a atualização contínua durante o quiz, sem comprometer a escalabilidade e a capacidade de adicionar novas funcionalidades.

O terceiro ainda estou em dúvida de qual aplicar. Possivelmente o *Template Method* ao implementar as interfaces de usuário, ou o *Strategy* para as operações, mas ainda não tenho certeza.

na hora de gerar o resultado final, na tela final da pntuação e acertos, fazer um templte da tela que segue um padrão de titulo, etc, mas a pontuação ser variada de acordo com o tema


---

## Gerador de quiz - parte 2

**Implementação python do gerador de quiz, contendo:**

- interface (primeira versão no terminal)
- utilização da base de questões
- carregar os dados, ler resposta do usuário, retornar se acertou ou errou

obs: colocar
- os 3 padrões de projetos escolhidos (código python)

**Factory:** deve ser usado para centralizar a criação de objetos Question a partir do JSON, promovendo a flexibilidade para futuras adições de tipos de questões e mantendo a lógica de criação separada da lógica principal.

modelar de alguma maneira que se eu quiser implementar um bd no lugar do json, só mudo no factory o método para o do banco e tudo certo

***singleton*: usar para ter apenas um acesso aoa arquivo json, para não ter que ficar abrindo e fechando toda hora**

**Strategy:** deve ser usado para separar a lógica de validação da resposta do usuário da lógica principal, permitindo que diferentes tipos de questões tenham diferentes formas de validação.





# Observações

https://www.youtube.com/results?search_query=cqrs+macoratti
