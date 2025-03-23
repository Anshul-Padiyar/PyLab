# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 

math = float(input("Enter math marks : "))
hindi = float(input("Enter hindi marks : "))
sanskrit = float(input("Enter sanskrit marks : "))

percent = round(((math + hindi + sanskrit) / 3), 2)

if (percent >= 40 and math >= 33 and hindi >= 33 and sanskrit >= 33):
    print("You PASS")
else:
    print("FAIL!")