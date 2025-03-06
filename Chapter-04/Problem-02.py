# Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

marks.append(int(input("Enter student marks: ")))
marks.append(int(input("Enter student marks: ")))
marks.append(int(input("Enter student marks: ")))
marks.append(int(input("Enter student marks: ")))
marks.append(int(input("Enter student marks: ")))
marks.append(int(input("Enter student marks: ")))

print("Marks before sorting:", marks)

marks.sort()

print("Marks after sorting:", marks)