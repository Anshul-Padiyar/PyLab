# 4. Write a program to find whether a given number is prime or not. 

num = int(input("Enter a number: ")) # Input: 2147483647

isPrime = True

if (num < 1):
    print("Invalid input!")  # Output: when number is less than 1
elif (num == 1):
    print(f"{num} is a prime number.")  # Output: when number is 1
else :
    for i in range(2, int(num/2)):
        if (num % i == 0):
            print(f"Divisor: {i}")  # Shows when a divisor is found
            isPrime = False
            break
    if (isPrime):
        print(f"{num} is a prime number.")  # Output: when number is prime
    else:
        print(f"{num} is not a prime number.")  # Output: when number is not prime