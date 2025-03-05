list02 = [2, 4, 8, 3, 0, 9, 1, 6, 5]

list02.insert(4, 7)
print("After insert:", list02)  # Output: [2, 4, 8, 3, 7, 0, 9, 1, 6, 5]

list02.remove(0)
print("After remove:", list02)  # Output: [2, 4, 8, 3, 7, 9, 1, 6, 5]

list02.reverse()
print("After reverse:", list02)  # Output: [5, 6, 1, 9, 7, 3, 8, 4, 2]

list02.append(10)
print("After append:", list02)  # Output: [5, 6, 1, 9, 7, 3, 8, 4, 2, 10]

print("Index of 10:", list02.index(10))  # Output: 9

print("Count of 7:", list02.count(7))  # Output: 1

list02.sort()
print("After sort:", list02)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# pop the element at index 9
print("Popped element:", list02.pop(9))  # Output: 10
print("After pop:", list02)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

list02.clear()
print("After clear:", list02)  # Output: []