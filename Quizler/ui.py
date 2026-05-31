from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        ### -------------- Label to show current score -----------##

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("arial", 16, "bold"))
        self.score_label.grid(row=0, column=1)

        ### ----------------- Canvas to display questions --------------------###

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Here is some question",
            fill=THEME_COLOR,
            font=("arial", 16, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        ###--------------------------- True button with image --------------------------###

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_press)
        self.true_button.grid(row=2, column=0)

        # False button with image
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_press)
        self.false_button.grid(row=2, column=1)

        #### ------------------------ Show first question-------------------------####

        self.get_next_question()

        self.window.mainloop()

    ### ------------------------------- Get the next question and update the screen------------------------###

    def get_next_question(self):

        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:

            ### -------------------- No more questions left -------------------------- ###

            self.canvas.itemconfig(self.question_text, text=" there is no more question :D")

    ### --------------------------- Called when user clicks True button ------------------------###

    def true_press(self):

        self.feedback(self.quiz.check_answer("True"))

    ### -------------------------------- Called when user clicks False button -------------------------###

    def false_press(self):

        self.feedback(self.quiz.check_answer("False"))

    ### --------------------- Show green for correct, red for wrong, then move to next question ---------------###

    def feedback(self, is_right):

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        ### --------------------------------- Wait 1 second, then load next question--------------------------###

        self.window.after(1000, self.get_next_question)