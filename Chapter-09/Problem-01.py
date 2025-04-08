#1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

with open("Chapter-09/poems.txt") as poems:
    poem = poems.read()
    if poem.count("twinkle"):
        print("Yes, It contains the word 'twinkle'\n")
    else :
        print("It do not contains the word ‘twinkle’\n")