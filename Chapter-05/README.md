# CHAPTER 5 – DICTIONARY & SETS

A dictionary is a collection of key-value pairs.

```python
dict = {
    "Cpp": True,
    "JavaScript": 2.0,
    "Java": 3,
    "Python": "Fourth"
}
print(dict["Cpp"])  # Output: True
print(dict["Python"])  # Output: Fourth
```

## PROPERTIES OF PYTHON DICTIONARIES

- Unordered: The items do not have a defined order.
- Mutable: You can change the items.
- Indexed: You can access items using keys.
- No duplicate keys: Each key must be unique.

## DICTIONARY METHODS

Consider the following dictionary:

```python
dict = {
    "Cpp": True,
    "JavaScript": 2.0,
    "Java": 3,
    "Python": "Fourth"
}
```

- `dict.items()`: Returns a list of (key, value) tuples.
- `dict.keys()`: Returns a list of the dictionary's keys.
- `dict.update({"Ruby": "Fifth"})`: Updates the dictionary with the provided key-value pair.
- `dict.get("JavaScript")`: Returns the value for the specified key.

More methods are available on [docs.python.org](https://docs.python.org).

# SETS IN PYTHON

A set is a collection of unique elements.

```python
s = set()  # empty set
s.add(1)
s.add(2)
print(s)  # Output: {1, 2}
```

If you are new to programming, you can think of sets as data types that contain unique values.

## PROPERTIES OF SETS

1. Unordered: The order of elements does not matter.
2. Unindexed: You cannot access elements by index.
3. Immutable elements: You cannot change items in sets.
4. No duplicate values: Each value must be unique.

## OPERATIONS ON SETS

Consider the following sets:

```python
set01 = {7, 3, 6, 7, 3, 8, 2, 0}
set02 = {4, 6, 9, 3, 2, 7, 1}
```

- `len(set01)`: Returns the number of elements in the set.
- `set01.remove(0)`: Removes the specified element from the set.
- `set02.pop()`: Removes and returns an arbitrary element from the set.
- `set01.clear()`: Empties the set.
- `set01.union(set02)`: Returns a new set with all items from both sets.
- `set01.intersection(set02)`: Returns a set with items common to both sets.