# 6. Write a program to calculate the factorial of a given number using for loop. 

num = int(input("Enter a number: "))
fact = 1
i = 1
while (i<=num):
    fact *= i
    i+= 1
print(f"The factorial of {num} is: {fact}")