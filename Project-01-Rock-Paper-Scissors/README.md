# Project 1: Rock, Paper, Scissors Game 🎮

A simple command-line game where you play Rock, Paper, Scissors against the computer.

## How to Play
1. Choose your move (1 for Rock, 2 for Paper, 3 for Scissors)
2. Computer will randomly pick its move
3. Winner is decided based on classic rules

## Game Rules
- Rock crushes Scissors ✊ > ✌️
- Scissors cuts Paper ✌️ > ✋
- Paper covers Rock ✋ > ✊
- Same moves = Tie 🤝

## Code Example

### Game Menu
```python
gameMenu = {
    0: "Exit", 
    1: "Rock", 
    2: "Paper", 
    3: "Scissors"
}
```

### Game Logic
```python
def whoWon(computerChose, userChose, computerScore, userScore):
    if (computerChose == userChose):
        print("It's a tie!")
    elif((computerChose == 1 and userChose == 2) or
         (computerChose == 2 and userChose == 3) or
         (computerChose == 3 and userChose == 1)):
        print("You won!")
        userScore += 1
    else:
        print("Computer won!")
        computerScore += 1
    return computerScore, userScore
```

## Features
- Score tracking
- Multiple rounds
- Input validation
- Clear menu system

## How to Run
1. Open terminal in project folder
2. Run `python main.py`
3. Follow on-screen instructions
4. Enter 0 to exit

## Sample Output
```
Round 1:
    1: Rock
    2: Paper
    3: Scissors
    0: Exit
Enter your choice (1, 2, 3 or 0): 1

You chose: Rock
Computer chose: Scissors

You won!
```