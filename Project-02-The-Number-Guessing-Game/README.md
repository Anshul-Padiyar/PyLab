# PROJECT 2: THE NUMBER GUESSING GAME 🎮

Have you ever tried to guess a secret number? We're going to create a computer game where the computer thinks of a number and you try to guess it!

## How to Play
1. Run the program
2. The computer will choose a random number between 1 and 100
3. Enter your guess when prompted
4. Follow the hints (higher/lower) to adjust your next guess
5. Keep guessing until you find the correct number
6. See how many attempts it took you to win!

## Game Rules
- The secret number is always between `lower_bound` and `upper_bound`
- You can guess any whole number in this range
- After each guess, you'll get one of three responses:
  * "Higher number please..." if your guess is too low
  * "Lower number please..." if your guess is too high
  * A winning message when you guess correctly
- The game tracks how many guesses you make

## Code Example
```python
import random

lower_bound = 1
upper_bound = 100
secret_number = random.randint(lower_bound, upper_bound)
number_of_guesses = 0

while True:
    guess = int(input("Enter Number: "))
    number_of_guesses += 1
    
    if secret_number > guess:
        print("Higher number please...")
    elif secret_number < guess:
        print("Lower number please...")
    else:
        break
```

## Features
- Random number generation between `lower_bound` - `upper_bound`
- Interactive user input
- Helpful feedback after each guess
- Guess counter to track performance
- Simple and intuitive interface

## Sample Output
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Enter Number: 50
Higher number please...

Enter Number: 75
Lower number please...

Enter Number: 65
Higher number please...

Enter Number: 70
Lower number please...

Enter Number: 67
Correct! You guessed the number in 5 guesses.
```