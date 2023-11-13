from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0


# Function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    """"checks answer against guess. Returns the number of turns remaining"""
    if guess > answer:
        print("Too High")
        return turns - 1

    elif guess < answer:
        print("Too low")
        return turns - 1

    else:
        print(f"You got it! The answer was {answer}")


# Make Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard : ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # Choosing the random number between 1 and 100
    print("Welcome to the Number Guessing Game")
    print("I am thinking of a number between 1 and 100")
    answer = randint(1, 100)
    # print(answer)

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess the number
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses")
            return
        elif guess != answer:
            print("Guess again")


game()