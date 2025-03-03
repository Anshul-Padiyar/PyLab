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

Some of the commonly used functions to perform operations on or manipulate strings are as follows. Let us assume there is a string ‘str’ as follows: 

str = 'harry' 

Now when operated on this string ‘str’, these functions do the following: 

1. len () function – This function returns the length of the strings. 

str = "harry" 

print(len(str))  # Output: 5 

2. String.endswith("rry") – This function_ tells whether the variable string ends with the string "rry" or not. If string is "harry", it returns true for "rry" since Harry ends with rry.

str = "harry" 

print(str.endswith("rry"))  # Output: True 

3. string.count("c") – counts the total number of occurrences of any character. 

str = "harry" 

count = str.count("r") 

print(count)  # Output: 2 

4. the first character of a given string. 

str = "harry" 

capitalized_string = str.capitalize() 

print(capitalized_string)  # Output: "Harry" 

5. string.find(word) – This function friends a word and returns the index of first occurrence of that word in the string. 

str = "harry" 

14 

index = str.find("rr") 

print(index)  # Output: 2 

6. string.replace (old word, new word ) – This function replace the old word with new word in the entire string. 

str = "harry" 

replaced_string = str.replace("r", "l")

print(replaced_string)  # Output: "hally" 

## ESCAPE SEQUENCE CHARACTERS 
Sequence of characters after backslash "\" → Escape Sequence characters Escape Sequence characters comprise of more than one character but represent one character when used within the strings.