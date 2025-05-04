# PROJECT 2: THE NUMBER GUESSING GAME

import random

lower_bound = 1
upper_bound = 100

secret_number = random.randint(lower_bound, upper_bound)

number_of_guesses = 0

print("\nWelcome to the Number Guessing Game!")
print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.\n")

while True:
    guess = int(input("Enter Number: "))
    number_of_guesses += 1
    
    if secret_number > guess:
        print("Higher number please...\n")
    elif secret_number < guess:
        print("Lower number please...\n")
    else :
        break

print(f"\nCorrect! You guessed the number in {number_of_guesses} guesses.")