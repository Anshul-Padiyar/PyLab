# 1. Write a program using functions to find greatest of three numbers.

def takeInput():
    return int(input("Enter a number: "))

def findGreatest(a, b, c) :
    if (a == b == c) :
        print("All are equal")
    elif (a <= b and c <= b) :
        print(f"{b} is greater")
    elif (b <= a and c <= a) :
        print(f"{a} is greater")
    else :
        print(f"{c} is greater")

a = takeInput()
b = takeInput()
c = takeInput()

findGreatest(a, b, c)