# 6. Write a python function which converts inches to cms.

def itoc(value):
    return value * 2.54

value = int(input("Enter the length to convert inch into centimeter: "))

print(f"{value} inch = {itoc(value)} cm")