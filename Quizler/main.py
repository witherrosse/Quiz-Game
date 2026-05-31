from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

### Create an empty list to store question objects ###

question_bank = []

### Loop through each question dictionary from data ###

for question in question_data:

    question_text = question["question"]
    question_answer = question["correct_answer"]

    ### Create a new Question object ###

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

### Create the quiz brain with all questions  ###

quiz = QuizBrain(question_bank)

### Create the user interface for the quiz ###

quiz_ui = QuizInterface(quiz)

## Show final results after quiz ends ###

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")