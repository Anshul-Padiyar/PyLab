# 2. Write a python program using function to convert Celsius to Fahrenheit.
def takeValue(): 
    return int(input("Enter the temperature: "))
def takeUnit(): 
    return input("Please enter the unit (e.g.: C, F): ")

def tempertureConvert(value, unit):
    if(unit.upper() == "C"):
        print(f"{value}C = {(value*1.8)+32}F")
    elif(unit.upper() == "F"):
        print(f"{value}F = {(value-32)*(5/9)}C")
    else :
        print("Invalid Entries!")

tempertureConvert(takeValue(), takeUnit())