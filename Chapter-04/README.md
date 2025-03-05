# CHAPTER 4 – LISTS AND TUPLES

Python lists are used to store multiple items in a single variable. Lists can contain items of different data types.

## LIST INDEXING

You can access elements of a list using their index, similar to strings.

```python
list01 = ["Apple", "Banana", 3.14, 2902, True, "Sherya", "Arjun"]
print(list01[0])  # Output: Apple
print(list01[1])  # Output: Banana
print(list01[70])  # Error: list index out of range
print(list01[0:2])  # Output: ['Apple', 'Banana']
```

## LIST METHODS

Here are some common list methods:

```python
list02 = [2, 4, 8, 3, 0, 9, 1, 6, 5]

list02.sort()
print(list02)  # Output: [0, 1, 2, 3, 4, 5, 6, 8, 9]

list02.reverse()
print(list02)  # Output: [9, 8, 6, 5, 4, 3, 2, 1, 0]

list02.append(10)
print(list02)  # Output: [9, 8, 6, 5, 4, 3, 2, 1, 0, 10]

list02.insert(4, 7)
print(list02)  # Output: [9, 8, 6, 5, 7, 4, 3, 2, 1, 0, 10]

list02.pop(2)
print(list02)  # Output: [9, 8, 5, 7, 4, 3, 2, 1, 0, 10]

list02.remove(10)
print(list02)  # Output: [9, 8, 5, 7, 4, 3, 2, 1, 0]
```

## TUPLES IN PYTHON

A tuple is a collection which is ordered and unchangeable.

```python
tuple01 = ()  # empty tuple
tuple02 = (1,)  # tuple with one element
tuple03 = (1, 7, 2)  # tuple with multiple elements
```

## TUPLE METHODS

Here are some common tuple methods:

```python
tuple04 = (1, 7, 2, 1)

print(tuple04.count(1))  # Output: 2 (1 appears twice)
print(tuple04.index(7))  # Output: 1 (7 is at index 1)
```