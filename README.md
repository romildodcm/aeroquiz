# aeroquiz

### Executar o projeto

```bash
git clone https://github.com/romildodcm/aeroquiz
sudo apt update
apt install python3.8-venv
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
uvicorn --reload main:app
```

Executando o projeto após prepração do ambiente:

```bash
source env/bin/activate
pip install -r requirements.txt
uvicorn --reload main:app
```

Alternativa para execução: `uvicorn main:app`
Ou selecionando a porta de execução no servidor: `uvicorn main:app --port 80 --host 0.0.0.0`

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



# Uso da API

## Obter todas as questões

### Request

`GET /perguntas`

http://62.72.9.154:8152/perguntas?theme=Aeronáutica&quantity=4

Query parameters:

- `theme=[string]`, sendo *Aeronáutica* ou *Aeroespacial*
- `quantity=[integer]`, sendo um número inteiro entre 1 e 10, indicando a quantidade de questões a serem retornadas, recomendado 5 ou 6.

Exemplo de resposta:

```JSON
[
    {
        "question_id": 11,
        "theme": "Aeronáutica",
        "difficulty": 1,
        "question": "Quem foi o pioneiro a voar num avião?",
        "options": [
            {
                "value": "Santos Dumont",
                "selected": false
            },
            {
                "value": "Orville Wright",
                "selected": false
            },
            {
                "value": "Wilbur Wright",
                "selected": false
            },
            {
                "value": "Charles Lindbergh",
                "selected": false
            }
        ]
    },
    {
        "question_id": 13,
        "theme": "Aeronáutica",
        "difficulty": 3,
        "question": "Qual é o avião comercial de passageiros mais vendido e amplamente utilizado no mundo?",
        "options": [
            {
                "value": "Boeing 747",
                "selected": false
            },
            {
                "value": "Airbus A380",
                "selected": false
            },
            {
                "value": "Boeing 737",
                "selected": false
            },
            {
                "value": "Airbus A320",
                "selected": false
            }
        ]
    },
    {
        "question_id": 17,
        "theme": "Aeronáutica",
        "difficulty": 1,
        "question": "Qual é a parte móvel na cauda de uma aeronave, projetada para controlar seu movimento em torno do eixo vertical?",
        "options": [
            {
                "value": "Aileron",
                "selected": false
            },
            {
                "value": "Elevator",
                "selected": false
            },
            {
                "value": "Rudder",
                "selected": false
            },
            {
                "value": "Flap",
                "selected": false
            }
        ]
    },
    {
        "question_id": 20,
        "theme": "Aeronáutica",
        "difficulty": 1,
        "question": "Quais são as três principais partes de uma aeronave?",
        "options": [
            {
                "value": "Motor, asas, leme",
                "selected": false
            },
            {
                "value": "Fuselagem, ailerons, leme",
                "selected": false
            },
            {
                "value": "Asas, leme, flaps",
                "selected": false
            },
            {
                "value": "Fuselagem, asas, empenagem",
                "selected": false
            }
        ]
    }
]
```

`POST /validar-respostas`

http://62.72.9.154:8152/validar-respostas

Com o body:

```JSON
[
    {
        "question_id": 11,
        "option": "Santos Dumont"
    },
    {
        "question_id": 13,
        "option": "Airbus A320"
    },
    {
        "question_id": 17,
        "option": "Elevator"
    },
    {
        "question_id": 20,
        "option": "Motor, asas, leme"
    }
]
```

e a resposta:

```JSON
{
    "score": 10,
    "correct_answers": 1,
    "questions": [
        {
            "question_id": 11,
            "theme": "Aeronáutica",
            "difficulty": 1,
            "score": 10,
            "question": "Quem foi o pioneiro a voar num avião?",
            "options": [
                {
                    "value": "Santos Dumont",
                    "is_correct": true,
                    "selected": true
                },
                {
                    "value": "Orville Wright",
                    "is_correct": false,
                    "selected": false
                },
                {
                    "value": "Wilbur Wright",
                    "is_correct": false,
                    "selected": false
                },
                {
                    "value": "Charles Lindbergh",
                    "is_correct": false,
                    "selected": false
                }
            ],
            "explanation": "Santos Dumont realizou o primeiro voo no “14 BIS”, primeiro avião mais pesado que o ar a conseguir decolar por meios próprios."
        },
        {
            "question_id": 13,
            "theme": "Aeronáutica",
            "difficulty": 3,
            "score": 3,
            "question": "Qual é o avião comercial de passageiros mais vendido e amplamente utilizado no mundo?",
            "options": [
                {
                    "value": "Boeing 747",
                    "is_correct": false,
                    "selected": false
                },
                {
                    "value": "Airbus A380",
                    "is_correct": false,
                    "selected": false
                },
                {
                    "value": "Boeing 737",
                    "is_correct": true,
                    "selected": false
                },
                {
                    "value": "Airbus A320",
                    "is_correct": false,
                    "selected": true
                }
            ],
            "explanation": "O Boeing 737 é um avião comercial muito vendido e amplamente utilizado em todo o mundo."
        },
        {
            "question_id": 17,
            "theme": "Aeronáutica",
            "difficulty": 1,
            "score": 10,
            "question": "Qual é a parte móvel na cauda de uma aeronave, projetada para controlar seu movimento em torno do eixo vertical?",
            "options": [
                {
                    "value": "Aileron",
                    "is_correct": false,
                    "selected": false
                },
                {
                    "value": "Elevator",
                    "is_correct": false,
                    "selected": true
                },
                {
                    "value": "Rudder",
                    "is_correct": true,
                    "selected": false
                },
                {
                    "value": "Flap",
                    "is_correct": false,
                    "selected": false
                }
            ],
            "explanation": "O leme (rudder) é a parte móvel na cauda de uma aeronave que controla o movimento em torno do eixo vertical."
        },
        {
            "question_id": 20,
            "theme": "Aeronáutica",
            "difficulty": 1,
            "score": 10,
            "question": "Quais são as três principais partes de uma aeronave?",
            "options": [
                {
                    "value": "Motor, asas, leme",
                    "is_correct": false,
                    "selected": true
                },
                {
                    "value": "Fuselagem, ailerons, leme",
                    "is_correct": false,
                    "selected": false
                },
                {
                    "value": "Asas, leme, flaps",
                    "is_correct": false,
                    "selected": false
                },
                {
                    "value": "Fuselagem, asas, empenagem",
                    "is_correct": true,
                    "selected": false
                }
            ],
            "explanation": "As três principais partes de uma aeronave são fuselagem, asas e empenagem (que inclui o leme)."
        }
    ]
}
```
