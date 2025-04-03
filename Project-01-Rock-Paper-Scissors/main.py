# PROJECT 1: ROCK, PAPER, SCISSORS GAME

import random

gameMenu = {0: "Exit", 1 : "Rock" , 2 : "Paper", 3 : "Scissors"}
choices = [1, 2, 3]
def printGameMenu():
    print(f" \t1: {gameMenu[1]} \n\t2: {gameMenu[2]} \n\t3: {gameMenu[3]} \n\t0: {gameMenu[0]}")

def whoWon(computerChose, userChose, computerScore, userScore) :
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

computerScore = 0
userScore = 0

def takeUserChose():
    userChose = int(input("Enter your chose (1, 2, 3 or 0) : "))
    if userChose not in gameMenu:
        print("Invalid input!")
        userChose = takeUserChose()
        return userChose
    else:
        return userChose
    
computerChose = 0
userChose = 1


gameRound = 1

while (userChose != 0):
    print(f"\nRound {gameRound}:")
    
    computerChose = random.choice(choices)
    
    printGameMenu()
    userChose = takeUserChose()
    
    print(f"\nYou chose : {gameMenu[userChose]}") 
    
    if(userChose != 0):
        print(f"Computer chose : {gameMenu[computerChose]}\n") 
        computerScore, userScore = whoWon(computerChose, userChose, computerScore, userScore)
        gameRound += 1
    

print("\nScores: ")
print(f"\tComputer : {computerScore}")
print(f"\tYou : {userScore}")