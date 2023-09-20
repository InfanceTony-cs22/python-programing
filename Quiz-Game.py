import random

# Sample question bank (you can expand this)
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Mercury"],
        "correct_answer": "Mars"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Leo Tolstoy"],
        "correct_answer": "William Shakespeare"
    }
]

def start_quiz():
    score = 0
    random.shuffle(questions)

    print("Welcome to the Quiz Game!")
    print("You will be presented with a series of questions. Choose the correct answer.")
    print("Let's begin!\n")

    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")

        user_answer = input("Enter the number of your answer: ")

        if user_answer.isdigit() and 1 <= int(user_answer) <= len(question["options"]):
            selected_option = question["options"][int(user_answer) - 1]
            if selected_option == question["correct_answer"]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong. The correct answer is: {question['correct_answer']}\n")
        else:
            print("Invalid input. Skipping to the next question.\n")

    print(f"Quiz completed! Your score is {score}/{len(questions)}.")

if __name__ == "__main__":
    start_quiz()
