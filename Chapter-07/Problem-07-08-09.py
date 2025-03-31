n = int(input("Enter a number: "))

# 7. Write a program to print the following star pattern.
print("\n--- Pattern 1 ---")
# for n = 3 
#   *
#  ***
# *****

for i in range(n):
    print(" "*(n-i), end="")
    print("*"*((i*2)+1), end="")
    print("")

# 8. Write a program to print the following star pattern:
print("\n--- Pattern 2 ---")
# *  
# * *  
# * * *       for n = 3 

for i in range(n):
    print("* "*(i+1))

# 9. Write a program to print the following star pattern. 
print("\n--- Pattern 3 ---")
# * * *  
# *    *    for n = 3 
# * * *   

for i in range(1, n+1):
    if(i==1 or n==i):
        print("*"*n) 
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
        print("")