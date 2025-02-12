def display_welcome_message():
    print("Welcome to the Country Capitals Quiz! 🌎")

def display_name_message(user_name):
    print(f"\n{user_name}, let’s see how many capitals you can guess correctly.\n")

def display_question(question, options):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            user_answer = int(input("\nChoose an option (1-4): "))
            if 1 <= user_answer <= 4:
                return user_answer
            else:
                print("Please choose a valid option between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def calculate_score(correct_answers):
    return correct_answers

def display_results(total_score, total_questions, user_name):
    print(f"\n{user_name}, you got {total_score} out of {total_questions} correct!")
    if total_score == total_questions:
        print("Congratulations, you're a geography master! 🏆")
    elif total_score >= total_questions // 2:
        print("Great job! You know your capitals well! 👍")
    else:
        print("Better luck next time! 🌍💪")

def display_thank_you_message():
    print("\nThank you for playing! Come back anytime to test your geography skills! 🙏")

def main():
    # Display the welcome message first
    display_welcome_message()

    # Ask for the user's name after the welcome message
    user_name = input("What is your name? ")

    # Greet the user with their name and introduce the quiz
    display_name_message(user_name)

    # List of questions, options, and correct answers
    questions = [
        ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 3),
        ("What is the capital of Japan?", ["Seoul", "Beijing", "Tokyo", "Kyoto"], 3),
        ("What is the capital of Australia?", ["Sydney", "Melbourne", "Canberra", "Brisbane"], 3),
        ("What is the capital of Brazil?", ["Sao Paulo", "Brasilia", "Rio de Janeiro", "Salvador"], 2),
        ("What is the capital of Canada?", ["Ottawa", "Toronto", "Vancouver", "Montreal"], 1),
        ("What is the capital of India?", ["New Delhi", "Mumbai", "Chennai", "Kolkata"], 1),
        ("What is the capital of Italy?", ["Florence", "Rome", "Milan", "Naples"], 2),
        ("What is the capital of Russia?", ["St. Petersburg", "Moscow", "Kazan", "Sochi"], 2),
        ("What is the capital of South Africa?", ["Cape Town", "Pretoria", "Johannesburg", "Durban"], 2),
        ("What is the capital of United States?", ["Los Angeles", "Washington D.C.", "New York", "Chicago"], 2)
    ]
    
    correct_answers = 0
    total_questions = len(questions)
    
    for question, options, correct_answer in questions:
        user_answer = display_question(question, options)
        if check_answer(user_answer, correct_answer):
            print("Correct answer! ✅")
            correct_answers += 1
        else:
            print(f"Wrong answer. The correct answer is option {correct_answer}. ❌")
    
    # Show the final results, including the user's name
    display_results(correct_answers, total_questions, user_name)
    display_thank_you_message()

if __name__ == "__main__":
    main()
