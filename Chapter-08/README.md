# Chapter 8: Functions & Recursion

Functions are reusable blocks of code that perform specific tasks. They help organize code and avoid repetition.

## Basic Function

The simplest function has no parameters:
```python
def sum():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(f"Sum of {a} and {b} is: ", a+b)

sum()  # Function call
```

## Functions with Arguments

Functions can accept parameters:
```python
# Simple greeting function
def greet(name, message):
    print(f"Hello {name}, {message}")

greet("AP", "What's up! All Good?")
```

## Default Arguments

Parameters can have default values:
```python
def adjust_vol(level, unit="dB"):
    print(f"Volume set to {level}{unit}")

adjust_vol(10)      # Uses default unit
adjust_vol(30, "%")  # Overrides default unit
```

## Practical Function Examples

### Temperature Converter
```python
def tempertureConvert(value, unit):
    if(unit.upper() == "C"):
        print(f"{value}C = {(value*1.8)+32}F")
    elif(unit.upper() == "F"):
        print(f"{value}F = {(value-32)*(5/9)}C")
```

### Unit Converter
```python
def itoc(value):
    return value * 2.54  # inches to centimeters
```

## Recursion

Recursion is when a function calls itself. It's useful for problems that can be broken down into similar sub-problems.

### Example: Factorial using Recursion
```python
def fact(n):
    if (n == 1 or n == 0):
        return 1
    return n * fact(n-1)
```

### Example: Sum of Natural Numbers
```python
def sumNum(n):
    if (n == 1):
        return 1
    return n + sumNum(n-1)
```

## Practice Problems
1. [Greatest of Three Numbers](./Problem-01.py)
2. [Temperature Converter](./Problem-02.py)
3. [Print Without Newline](./Problem-03.py)
4. [Recursive Sum](./Problem-04.py)
5. [Length Converter](./Problem-06.py)