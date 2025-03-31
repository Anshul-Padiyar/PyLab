# 10. Write a program to print multiplication table of n using for loops in reversed order.

num = int(input("Enter a number: "))

print(f"Multiplication table for {num}:")
for i in range(1, 11) :
    print(f"{num} x {11-i} = ", (num*(11-i)))