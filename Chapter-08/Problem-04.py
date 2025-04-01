# 4. Write a recursive function to calculate the sum of first n natural numbers.
def takeInput():
    return int(input("Enter a number: "))

def sumNum(n):
    if (n == 1):
        return 1
    return n + sumNum(n-1)

n = takeInput()

print(f"The sum of first {n} natural numbers is: {sumNum(n)}")
#Output: The sum of first 996 natural numbers is: 496506