from question_model import Question
from data import question_data

def create_question_bank(data):
    """Convert data dicts to Question objects."""
    return [Question(q["text"], q["answer"]) for q in data]

def run_quiz():
    """Run the quiz game."""
    question_bank = create_question_bank(question_data)
    score = 0

    print("❓ Welcome to the Quiz Game!\n")
    for idx, question in enumerate(question_bank, start=1):
        print(f"Q{idx}: {question.text}")
        user_answer = input("Your answer: ")
        if question.check_answer(user_answer):
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {question.answer}\n")

    print(f"🏆 Quiz finished! Your final score: {score}/{len(question_bank)}")

if __name__ == "__main__":
    run_quiz()
