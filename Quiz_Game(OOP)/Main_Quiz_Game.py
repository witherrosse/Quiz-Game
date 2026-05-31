from QuizBrain import QuizBrain
from question_model import Question
from data_for_quiz import question_data

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.NextQuestion()


print(f"you're final score is {quiz.score}/ {quiz.question_number}")


