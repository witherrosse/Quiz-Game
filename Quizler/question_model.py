class Question:

    ### This function runs when a new Question object is created ###

    def __init__(self, q_text, q_answer):

        ### Store the question text ###

        self.text = q_text

        #### Store the correct answer (True/False) ###

        self.answer = q_answer