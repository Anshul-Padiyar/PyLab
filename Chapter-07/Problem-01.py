# 1. Write a program to print multiplication table of a given number using for loop. 

num = int(input("Enter a number: "))

i = 1

print(f"Multiplication table for {num}:")
while(i <= 10) :
    print(f"{num} x {i} = ", (num*i))
    i+=1