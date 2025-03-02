# Chapter 2 – Variables and Data Types

A variable is the name given to a memory location in a program.

## Data Types

Primarily, these are the following data types in Python:
1. Integers
2. Floating point numbers
3. Strings
4. Booleans
5. None

Python is a fantastic language that automatically identifies the type of data for us.
```python
a = 71 # identifies a as class <int>
b = 88.44 # identifies b as class <float>
name = "Anshul" # identifies name as class <str>
```

## Rules for Choosing an Identifier

- A variable name can contain alphabets, digits, and underscores.
- A variable name can only start with an alphabet and underscores.
- A variable name can’t start with a digit.
- No whitespace is allowed to be used inside a variable name.

Examples of a few variable names are: `Anshul`, `one8`, `seven`, `_seven`, etc.

## Operators in Python

Following are some common operators in Python:
1. Arithmetic operators: `+`, `-`, `*`, `/`, `%`.
2. Assignment operators: `=`, `+=`, `-=`, etc.
3. Comparison operators: `==`, `>`, `>=`, `<`, `!=`, etc.
4. Logical operators: `and`, `or`, `not`.

## `type()` Function and Typecasting

The `type()` function is used to find the data type of a given variable in Python.
```python
a = 31
type(a) # class <int>
b = "31"
type(b) # class <str>
```

A number can be converted into a string and vice versa (if possible). There are many functions to convert one data type into another.
```python
str(31)    # "31"   # integer to string conversion
int("32")  # 32     # string to integer conversion
float(32)  # 32.0   # integer to float conversion
```

Here `"31"` is a string literal and `31` is a numeric literal.

## `input()` Function

This function allows the user to take input from the keyboard as a string.
```python
a = input("Enter name : ")
```
> It is important to note that the output of `input` is always a string (even if a number is entered).