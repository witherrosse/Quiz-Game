How this code works (Quizler - True/False Quiz App)
This is a graphical true/false quiz application using Tkinter. It gets questions from the Open Trivia Database API and lets the user answer with True or False buttons.

________________________________________________________________________________

Project files
This project is made of 4 files:

question_model.py – defines what a Question object looks like

quiz_brain.py – handles the quiz logic (score, next question, check answer)

ui.py – creates the graphical user interface

main.py – brings everything together and runs the quiz

What is used in this code
tkinter module: to create the window, buttons, canvas, and labels

html module: to clean up text with HTML entities (like &quot;)

requests module: to get questions from the online API

class and object: to organize the code into reusable parts

PhotoImage: to put images on buttons

.after() method: to delay the next question by 1 second

___________________________________________________________________________________________________
 
How the quiz works
Program starts (main.py)

It gets question data from data.py (which comes from the API)

Creates a Question object for each question

Stores all questions in a list called question_bank

Creates a QuizBrain object with the question bank

Creates a QuizInterface object and passes the QuizBrain to it

User sees the window (ui.py)

A window with title "Quizler" opens

Shows a score label (top right)

Shows a white canvas with the first question

Shows a True button and a False button with images

User answers a question

User clicks True or False button

quiz_brain.py checks if the answer is correct

Score increases if correct

Canvas turns green (correct) or red (wrong) for 1 second

Then the next question appears automatically

Quiz ends

When no more questions are left, the canvas shows "there is no more question :D"

Final score is printed in the terminal

How each file works
question_model.py

Has a class called Question

Each question has text and answer (True/False)

quiz_brain.py

Has a class called QuizBrain

Keeps track of question_number and score

still_has_questions(): checks if there are more questions

next_question(): returns the next question text

check_answer(): compares user answer with correct answer

ui.py

Has a class called QuizInterface

Creates all buttons, labels, and canvas

get_next_question(): updates screen with new question

feedback(): shows green or red background

Uses .after(1000, ...) to wait before next question
