# Blackjack House rules
# Deck is unlimitted in size
# There are no jokers
# The Jack / Queen / King all count as 10
# Use the following list as 11 or 1
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn
# Cards are not removed from the deck as they are drawn

import random
import os
# Hint 1:
# create a deal_card() function that uses the list to return a random card
# 11 is ace
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  """Returns a rendom card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

# Hint 3:
# Create a function called calculate_score() that takes a list of cards as input and returns the score
# Look up the sum() function
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  # Hint 4:
  #Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjac in our game.
  # if 11 in cards and 10 in cards and len(cards) ==2: =>this line can be written as
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  # Hint 5
  # inside calculate_score() check for an 11 {ace}. If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

# Hint 10:
# Create a Function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If
# the computer has a blackjack(0), then the user wins. If the user_score is over 21, then the user loses. If computer_score is over 21. then the computer loses.
# If none of the above, then the player with the highest score wins.
def compare(user_score , computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif user_score == 0:
    return "Win with a Blackjack"
  elif user_score > 21:
    return "You went over, You lose"
  elif computer_score > 21:
    return "Opponent went over, You win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"

def play_game():
  # Hint 2:
  # Deal the user and computer 2 cards each using deal_card()
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    # new_card = deal_card()
    # user_cards.append(new_card)
    # the above code can be done as below
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  # Hint 8:
  # The score will need to be rechecked with every new card drawn and the checks in Hint 6 need to be repeated until the game ends
  while not is_game_over:

    # Hint 6:
    #  call calculate_score(). If the computer or the user has a blackjack {0} or if the user's choice is over 21, then the game ends
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"    Your cards: {user_cards}, current score = {user_score}")
    print(f"    computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True

    # Hint 7:
    # If the game has not ended, ask theuser if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards list. If no, then the game has ended
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  # Hint 9:
  # Once the user is done and no longer wants to draw more cards, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"    Your final hand: {user_cards}, final score = {user_score}")
  print(f"    computer's final hand: {computer_cards[0]}, final score: {computer_score}")
  print(compare(user_score , computer_score))

# Hint 10:
# Ask the user if they want to restart the game. If they ansuer yes, clear the console and start a new game of black jack.
while input("Do you want to play a game of Blackjack? Type 'y' on 'n' : ").lower() == "y":
  os.system('CLS')
  play_game()