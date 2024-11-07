import random


def random_number(min, max):
    """
    Generate Random number between two values.
    """
    return random.randint(min, max)


def random_symbol():
    """
    Generate Random symbol between: +, -, *.
    """
    return random.choice(['+', '-', '*'])


def generate_operation(number1, number2, symbol):
    """
    Creates an operation with the numbers and the symbol generates before
    """
    problem = f"{number1} {symbol} {number2}"
    if symbol == '+': solution = number1 + number2
    elif symbol == '-': solution = number1 - number2
    else: solution = number1 * number2
    return problem, solution

def math_quiz():
    """
    Runs a math quiz where the user must answer randomly generated math problems
    """
    points = 0
    number_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(number_questions):
        #Generate two random numbers and one symbol
        number1 = random_number(1, 10)
        number2 = random_number(1, 5)
        symbol = random_symbol()

        #Generate the operation and resolves it
        problem, solution = generate_operation(number1, number2, symbol)
        print(f"\nQuestion: {problem}")

        # Error handling for user input
        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)

        except ValueError:
            print("Error: Invalid input. Please enter an integer.")
            continue  # Skip to the next question if input is invalid

        # Check if the user's answer is correct
        if useranswer == solution:
            print("Correct! You earned a point.")
            points += 1
        else:
            print(f"Wrong answer. The correct answer is {solution}.")
    #Display the final score after all the questions
    print(f"\nGame over! Your score is: {points}/{number_questions}")

if __name__ == "__main__":
    math_quiz()
