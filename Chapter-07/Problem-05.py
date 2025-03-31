# 5. Write a program to find the sum of first n natural numbers using while loop. 

num = int(input("Enter a number: "))
s = 0
i = 1
while (i<=num):
    s += i
    i+= 1
print(f"The sum of first {num} natural numbers is: {s}")