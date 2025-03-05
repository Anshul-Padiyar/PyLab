l2 = [2, 4, 8, 3, 0, 9, 1, 6, 5]

l2.insert(4, 7)
print("After insert:", l2)  # Output: [2, 4, 8, 3, 7, 0, 9, 1, 6, 5]

l2.remove(0)
print("After remove:", l2)  # Output: [2, 4, 8, 3, 7, 9, 1, 6, 5]

l2.reverse()
print("After reverse:", l2)  # Output: [5, 6, 1, 9, 7, 3, 8, 4, 2]

l2.append(10)
print("After append:", l2)  # Output: [5, 6, 1, 9, 7, 3, 8, 4, 2, 10]

print("Index of 10:", l2.index(10))  # Output: 9

print("Count of 7:", l2.count(7))  # Output: 1

l2.sort()
print("After sort:", l2)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Pop the element at index 9
print("Popped element:", l2.pop(9))  # Output: 10
print("After pop:", l2)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

l2.clear()
print("After clear:", l2)  # Output: []