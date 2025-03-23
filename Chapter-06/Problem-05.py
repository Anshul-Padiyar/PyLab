# 5. Write a program which finds out whether a given name is present in a list or not. 

names = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf"]

name = input("Enter your name : ")

if ( name in names):
    print("Your name is in the list")
else :
    print("Your name is not in the list")