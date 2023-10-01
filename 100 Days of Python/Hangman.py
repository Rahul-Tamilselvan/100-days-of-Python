import random

# importing the words from Hangman_words file
from Hangman_words import word_list
word = random.choice(word_list).lower()
# print(word)

# Determining the no of lives
lives = 6

# print the no of "_" as the chosen word
display = []
for letter in word:  # for _ in range(len(word))
    display.append("_")
    # or display += "_"
print(display)

# set a variable to check for condition
end_of_game = False

# looping the choices
while not end_of_game:
    # Getting input from the user
    guess = input("Guess a letter : ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    # Replace the "_" with the input from the user
    for position in range(len(word)):
        letter = word[position]
        if guess == letter:
            display[position] = guess
    print(display)

    if guess not in word:
        print(f"You guessed {guess}, that's not in the word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
            print(f"The word is {word}")

        # importing stages from Hangman_stages file
        from Hangman_stages import stages
        print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(lives)

