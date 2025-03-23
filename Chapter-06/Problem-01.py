# 1. Write a program to find the greatest of four numbers entered by the user.

num01 = int(input("Enter 1st number : "))
num02 = int(input("Enter 2nd number : "))
num03 = int(input("Enter 3rd number : "))
num04 = int(input("Enter 4th number : "))

if num01 >= num02 and num01 >= num03 and num01 >= num04:
    greatest = num01
elif num02 >= num01 and num02 >= num03 and num02 >= num04:
    greatest = num02
elif num03 >= num01 and num03 >= num02 and num03 >= num04:
    greatest = num03
else:
    greatest = num04

print(f"{greatest} is the greatest number")