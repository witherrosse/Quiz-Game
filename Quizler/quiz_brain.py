import html

class QuizBrain:

    ### Initialize the quiz with a list of questions ###

    def __init__(self, q_list):

        self.question_number = 0      ### Track which question we are on ##
        self.score = 0                ### Track how many correct answers ###
        self.question_list = q_list   ### All questions in the quiz ###
        self.current_question = None  ### The question currently being asked ###

    ### Check if there are more questions to ask ###

    def still_has_questions(self):

        return self.question_number < len(self.question_list)

    ### Get the next question and return it as a string ###

    def next_question(self):

        self.current_question = self.question_list[self.question_number]
        self.question_number += 1

        ### Remove HTML entities like &quot; from the text ###

        q_text = html.unescape(self.current_question.text)

        return f"Q.{self.question_number} : {q_text}"

    ###  Check if the user's answer matches the correct answer ###

    def check_answer(self, user_answer):

        correct_answer = self.current_question.answer

        ###  Compare answers (case insensitive) ###

        if user_answer.lower() == correct_answer.lower():

            self.score += 1
            return True
        else:
            return False