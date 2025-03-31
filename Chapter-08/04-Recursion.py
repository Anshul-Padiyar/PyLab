""" 
Factorial (0) = 1
Factorial (1) = 1
Factorial (2) = 2 x 1
Factorial (3) = 3 x 2 x 1
Factorial (4) = 4 x 3 x 2 x 1
Factorial (5) = 5 x 4 x 3 x 2 x 1
Factorial (n) = n x (n-1) x ..... x 3 x 2 x 1

Factorial (n) = n x Factorial(n-1)
"""

def fact(n):
    if (n ==1 or n == 0):
        return 1
    return n * fact(n-1)         # Function calling itself 

n = int(input("Enter a number: "))
print(f"Factorial of {n} is: {fact(n)}")