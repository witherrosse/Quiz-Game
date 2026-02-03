class Question:
    """Represents a single quiz question."""

    def __init__(self, text: str, answer: str):
        self.text = text
        self.answer = answer

    def check_answer(self, user_answer: str) -> bool:
        """Return True if user_answer matches the correct answer."""
        return user_answer.strip().lower() == self.answer.strip().lower()
