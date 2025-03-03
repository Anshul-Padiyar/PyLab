# CHAPTER 3 – STRINGS

String is a data type in python. String is a sequence of characters enclosed in quotes. 

We can primarily write a string in these three ways. 

```python
str01 = "God is great!"; # Single quoted string
str02 = 'God is great!'; # Double quoted string
str03 = '''God is great!'''; # Triple quoted string
```

> Strings are immutable

## STRING SLICING 

You can slice a string in Python to get a part of it.

Consider the following string:

```python
str01 = "God is great!"
```

The index in a string starts from 0 to (length - 1) in Python. To slice a string, use the following syntax:

```python
substring = str01[start:stop]
```

For example:

```python
substring = str01[0:3]
print(substring)  # Output: God
```

Negative indices can also be used. For example:

```python
substring = str01[-6:-1]
print(substring)  # Output: great
```

Here, -1 corresponds to the last character, -2 to the second last, and so on.

## SLICING WITH SKIP VALUE

You can also slice a string with a skip value. This means you can skip characters while slicing. The syntax is:

```python
substring = string[start:stop:skip]
```

For example:

```python
word = "feeling-upset-physically-and-mentally-with-anticipatory-excitement-and-anxiety"
skipword = word[9:45:3]
print(skipword)  # Output: pthil-deayi-
```

Here, the slice starts at index 9, stops at index 45, and skips every 3rd character.

Other advanced slicing techniques:

```python
word = "feeling-upset-physically-and-mentally-with-anticipatory-excitement-and-anxiety"
substring = word[:7]
print(substring)  # Output: feeling

substring = word[71:]
print(substring)  # Output: anxiety
```

In the first example, the slice starts from the beginning and stops at index 7. In the second example, the slice starts at index 71 and goes to the end of the string.


## STRING FUNCTIONS

Here are some commonly used functions to work with strings. Let's use the string `string = "God is great!"` for the examples:

1. `len()` function – This function returns the length of the string.

```python
print(len(string))  # Output: 13
```

2. `string.startswith("God")` – This function checks if the string starts with "God".

```python
print(string.startswith("God"))  # Output: True
```

3. `string.endswith("great")` – This function checks if the string ends with "great".

```python
print(string.endswith("great"))  # Output: False
```

4. `string.count("g")` – This function counts the number of occurrences of the character "g".

```python
print(string.count("g"))  # Output: 1
```

5. `string.index("g")` – This function returns the index of the first occurrence of the character "g".

```python
print(string.index("g"))  # Output: 6
```

6. `string.capitalize()` – This function capitalizes the first character of the string.

```python
print(string.capitalize())  # Output: "God is great!"
```

7. `string.lower()` – This function converts all characters in the string to lowercase.

```python
print(string.lower())  # Output: "god is great!"
```

8. `string.upper()` – This function converts all characters in the string to uppercase.

```python
print(string.upper())  # Output: "GOD IS GREAT!"
```

9. `string.replace("great", "cool")` – This function replaces the word "great" with "cool" in the string.

```python
print(string.replace("great", "cool"))  # Output: "God is cool!"
```

10. `string.find("great")` – This function finds the word "great" and returns the index of its first occurrence.

```python
print(string.find("great"))  # Output: 7
```

## ESCAPE SEQUENCE CHARACTERS 
Sequence of characters after backslash "\" → Escape Sequence characters Escape Sequence characters comprise of more than one character but represent one character when used within the strings.