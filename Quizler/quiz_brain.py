import html

class QuizBrain:

    

    def __init__(self, q_list):

        ''' Initialize the quiz with a list of questions '''

        self.question_number = 0      
        self.score = 0                
        self.question_list = q_list   
        self.current_question = None  

    

    def still_has_questions(self):

        ''' Check if there are more questions to ask '''

        return self.question_number < len(self.question_list)

    

    def next_question(self):

        ''' Get the next question and return it as a string '''

        self.current_question = self.question_list[self.question_number]
        self.question_number += 1

        ### Remove HTML entities like &quot; from the text ###

        q_text = html.unescape(self.current_question.text)

        return f"Q.{self.question_number} : {q_text}"

    

    def check_answer(self, user_answer):

        ''' Check if the user's answer matches the correct answer '''

        correct_answer = self.current_question.answer

        

        if user_answer.lower() == correct_answer.lower():

            self.score += 1
            return True
        else:
            return False
