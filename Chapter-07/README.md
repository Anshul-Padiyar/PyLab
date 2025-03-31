# Chapter 7: Loops in Python

Loops help us repeat tasks without writing the same code multiple times.

## Types of Loops

### 1. While Loop
Repeats code while a condition is true.

```python
# Example: Print multiplication table
num = 5
i = 1
while(i <= 10):
    print(f"{num} x {i} = {num*i}")
    i += 1
```

### 2. For Loop
Used to iterate through sequences (lists, strings, etc.).

```python
# Example: Greeting names starting with 'B'
names = ["Alpha", "Bravo", "Charlie"]
for name in names:
    if name.startswith("B"):
        print(f"Hello {name}!")
```

## Important Loop Concepts

### Range Function
```python
# Prints 0 to 4
for i in range(5):
    print(i)
```

### Break Statement
Exits the loop immediately.
```python
# Example: Check if number is prime
for i in range(2, num):
    if num % i == 0:
        print("Not prime")
        break
```

### Continue Statement
Skips current iteration.
```python
# Print only odd numbers
for i in range(5):
    if i % 2 == 0:
        continue
    print(i)
```

## Pattern Printing Examples
```python
# Simple Triangle Pattern
n = 3
for i in range(n):
    print("* " * (i+1))

# Output:
# *
# * *
# * * *
```

## Practice Problems
1. [Multiplication Table](./Problem-01.py)
2. [Name Greeter](./Problem-02.py)
3. [Prime Number Checker](./Problem-04.py)
4. [Factorial Calculator](./Problem-06.py)
5. [Pattern Printing](./Problem-07-08-09.py)