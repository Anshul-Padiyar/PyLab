# Chapter 6 - Conditional Expressions in Python

We make decisions every day based on conditions:
- If it's Sunday, we might play games
- If it's sunny, we might get ice cream
- If we have permission, we might go hiking

In Python, we use conditional statements to make similar decisions in our code.

## Basic If-Else Statement

The simplest form is an if-else statement:

```python
# Simple number comparison
a = 22
if(a > 9):
    print("greater")
else:
    print("lesser")
```

## If-Elif-Else Chain

When you need multiple conditions, use elif (else if):

```python
# Grade calculation example from Problem-06
marks = int(input("Enter student marks : "))

if (marks >= 91):
    print("Grade: A+")
elif (marks >= 81):
    print("Grade: A")
elif (marks >= 61):
    print("Grade: B")
elif (marks >= 46):
    print("Grade: C")
elif (marks >= 33):
    print("Grade: D")
else:
    print("Grade: F")
```

## Comparison Operators

- `==` : Equal to
- `!=` : Not equal to
- `>` : Greater than
- `>=` : Greater than or equal to
- `<` : Less than
- `<=` : Less than or equal to

## Logical Operators

- `and`: Both conditions must be True
- `or`: At least one condition must be True
- `not`: Inverts True to False and vice versa

Example using logical operators:
```python
# From Problem-02
if (percent >= 40 and math >= 33 and hindi >= 33 and sanskrit >= 33):
    print("You PASS")
else:
    print("FAIL!")
```

## Membership Testing

You can check if something exists in a list using `in`:

```python
# From Problem-05
names = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
name = "Charlie"

if (name in names):
    print("Your name is in the list")
else:
    print("Your name is not in the list")
```

## String Operations with Conditions

String comparisons are case-sensitive. Use `.lower()` for case-insensitive comparison:

```python
# From Problem-07
post = "I love Deadpool movies!"
if ("deadpool" in post.lower()):
    print("This post talks about Deadpool")
```

## Important Notes

1. Indentation is crucial in Python - use consistent spacing for code blocks
2. You can have any number of elif statements
3. The else block is optional and runs only if all previous conditions are False
4. Conditions are checked in order from top to bottom