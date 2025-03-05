"""
PC103_CSE110 
W04 Project: Word Puzzle  
Author: Tiago Borges 

"""

# Word Puzzle Game
# Added Feature: The game selects a random word from a predefined list of words for added variety.

# In this project, I aimed to create a word guessing game similar to Wordle
# My main concerns were understanding how to handle string comparisons effectively 
# and how to provide meaningful hints to the user. 
# I was also challenged by implementing the logic to differentiate between correct letters 
# in the correct position, correct letters in the wrong position, and incorrect letters.

#Let's do it!


import random

# List of words
words = ["temple", "moroni", "mosiah", "zion", "prophet", "faith"]

# Choose a random word
secret_word = random.choice(words)

guess_count = 0

print("Welcome to the word guessing game!")

# Function to generate hint
def generate_hint(secret_word, guess):
    # Check if the length of the secret word and guess are the same
    if len(secret_word) != len(guess):
        print("The guess must have the same length as the secret word.")
        return None
    
    # Create the initial hint with underscores
    hint = ['_'] * len(secret_word)
    
    # First pass: Check for exact matches (uppercase)
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint[i] = secret_word[i].upper()  # Exact match (uppercase)
    
    # Second pass: Check for misplaced letters (lowercase)
    for i in range(len(secret_word)):
        if hint[i] == '_':  # Only check positions that are still underscores
            if guess[i] in secret_word:
                hint[i] = guess[i].lower()  # Misplaced letter (lowercase)
    
    # Return the hint with spaces between characters
    return " ".join(hint)

# Initial hint with underscores
print("Your hint is:", " ".join(['_'] * len(secret_word)))

# Loop until the user guesses correctly
while True:
    guess = input("What is your guess? ").lower()
    guess_count += 1
    
    # Generate the hint
    hint = generate_hint(secret_word, guess)
    
    if hint:  # If the hint is generated correctly
        print(f"Your hint is: {hint}")
    
    if guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {guess_count} guesses.")
        break
    else:
        print("Your guess was not correct.")

# Through this project, I achieved a deeper understanding of loops, conditionals, and string manipulation in Python. 
# I successfully implemented the hint system, including uppercase for correct positions, 
# lowercase for correct letters in wrong positions, and underscores for incorrect letters. 
# Additionally, I enhanced the program by adding a random word selection feature, which makes the game more dynamic. 
# This assignment helped me improve my problem-solving skills and confidence in writing Python code.

# Thank you for taking the time to review and correct my work!
# I pray that Heavenly Father may bless you for your dedication and support.
