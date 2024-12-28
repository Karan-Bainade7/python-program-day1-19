# KBC Program in Python
def play_kbc():
    # Questions, options, and correct answers
    questions = [
        "What is the capital of India?",
        "Which planet is known as the Red Planet?",
        "Who wrote the play 'Romeo and Juliet'?",
        "What is the square root of 64?",
        "Which is the smallest prime number?"
    ]

    options = [
        ["1. Delhi", "2. Mumbai", "3. Kolkata", "4. Chennai"],
        ["1. Earth", "2. Mars", "3. Jupiter", "4. Venus"],
        ["1. William Shakespeare", "2. Charles Dickens", "3. Jane Austen", "4. Mark Twain"],
        ["1. 6", "2. 7", "3. 8", "4. 9"],
        ["1. 0", "2. 1", "3. 2", "4. 3"]
    ]

    answers = [1, 2, 1, 3, 3]  # Correct option numbers

    # Prize money for each question
    prize_money = [1000, 5000, 10000, 20000, 50000]

    total_prize = 0

    print("Welcome to Kaun Banega Crorepati!\n")

    for i in range(len(questions)):
        print(f"Q{i + 1}: {questions[i]}")
        for option in options[i]:
            print(option)

        try:
            # Get user's answer
            user_answer = int(input("Enter your answer (1-4): "))
            if user_answer == answers[i]:
                total_prize += prize_money[i]
                print(f"Correct! You have won Rs. {prize_money[i]}\n")
            else:
                print("Wrong answer! Game over.")
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            break

    print(f"You are taking home Rs. {total_prize}. Congratulations!")

# Start the game
play_kbc()
