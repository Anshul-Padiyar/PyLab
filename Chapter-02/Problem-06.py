# Write a python program to calculate the square of a number entered by the user.

a = int(input("Enter a number : "))

print("Square of the number is", a * a) # Using multiplication
print("Square of the number is", a ** 2) # Using exponentiation

# Incorrect for calculating the square, it performs a bitwise XOR operation
print("Square of the number is", a ^ 2)