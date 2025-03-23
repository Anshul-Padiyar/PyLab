# 6. Write a program to calculate the grade of a student from his marks from the following scheme: 
# 100 - 91 => A+
# 90 - 81 => A 
# 80 - 61 => B 
# 60 - 46 => C 
# 45 - 33 => D 
# 00 - 32 => F 

marks = int(input("Enter student marks : "))

if (marks > 100 or marks < 0):
    print("Invalid input!")
elif (marks >= 91):
    print("Grade: A+")
elif (marks>=81):
    print("Grade: A")
elif (marks>=61):
    print("Grade: B")
elif (marks>=46):
    print("Grade: C")
elif (marks>=33):
    print("Grade: D")
else:
    print("Grade: F")