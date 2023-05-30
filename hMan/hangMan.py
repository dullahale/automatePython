# This is a file that contains hangman project.

import random as rand
from hangMan_words import word_list as wordList
from hangMan_art import stages as stages
from hangMan_art import logo as logo
import clear as clear

chosen_word = rand.choice(wordList)

# Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.

lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

# Uncomment to see the word
print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'. So if the
# chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
length_of_word = len(chosen_word)
for i in range(length_of_word):
    display += "_"

# Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the
# letters in the chosen_word and 'display' has no more blanks ("_").
# Then you can tell the user they've won.
endOfGame = 0
while endOfGame == 0:
    guess = input("Guess a letter: ").lower()

# If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed {guess}")


# Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

    for position in range(length_of_word):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

# If guess is not a letter in the chosen_word,
# Then reduce 'lives' by 1.
# If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        print(f"You've guessed this letter {guess}, thats not in the word therefore you lose a life")
        lives -= 1
        if lives == 0:
            endOfGame = 1
            print("You lose!!!")


# Print 'display' and you should see the guessed letter in the
# correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
    print("".join(display))

    # Checking if user has all the letters
    if "_" not in display:
        endOfGame = 1
        print("You Win!!!!")

    print(stages[lives])

