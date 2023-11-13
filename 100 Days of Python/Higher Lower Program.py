from game_data_higher_lower import data
import random
import os

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


def format_data(account):
    """Takes the account data  and returns the printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


# #Use if statement to check if user is correct
def check_answer(guess, a_followers, b_follower):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_follower:
        # if guess == 'a':
        # return True
        # above two lines can be written as
        return guess == 'a'
    else:
        return guess == 'b'


score = 0
game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable
while game_should_continue:

    # Generate a random account from the game data

    # Making the account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    # #Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen between the rounds.
    os.system("CLS")

    # Give user feedback on their guess.
    # Score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current Score {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
