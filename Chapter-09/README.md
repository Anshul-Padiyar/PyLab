# Chapter 9: File Input/Output in Python

Learn how to work with files in Python - reading, writing, and managing data.

## Basic File Operations

### 1. Writing to Files
```python
# Create and write to a file
file = open("file.txt", "w")
file.write("Hello World!")
file.close()

# Better way using 'with' statement
with open("file.txt", "w") as file:
    file.write("Hello World!")  # Automatically closes the file
```

### 2. Reading Files
```python
# Read entire file
with open("file.txt") as file:
    content = file.read()
    print(content)

# Read line by line
with open("file.txt") as file:
    for line in file:
        print(line)
```

## File Opening Modes

| Mode | Description |
|------|-------------|
| 'r'  | Read (default) |
| 'w'  | Write (overwrites) |
| 'a'  | Append |
| 'r+' | Read & Write |
| 'w+' | Write & Read |
| 'a+' | Append & Read |

## Practical Examples

### Example 1: Search in File
```python
# Search for a word in file
with open("poems.txt") as poems:
    poem = poems.read()
    if "twinkle" in poem:
        print("Word found!")
```

### Example 2: Generate Multiple Files
```python
# Create multiplication tables
for num in range(2, 21):
    with open(f"table_{num}.txt", "w") as file:
        for i in range(1, 11):
            file.write(f"{num} x {i} = {num*i}\n")
```

### Example 3: Filter File Content
```python
# Read lines starting with specific letter
with open("input.txt") as file:
    for line in file:
        if line.strip().lower().startswith('a'):
            print(line)
```

## Best Practices
1. Always use `with` statement (auto-closes files)
2. Handle file not found errors
3. Choose appropriate file modes
4. Close files when using manual open()

## Practice Problems
1. [Word Search in File](./Problem-01.py)
2. [Line Filter Program](./Problem-02.py)
3. [Table Generator](./Problem-03.py)