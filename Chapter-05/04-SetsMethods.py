set01 = {7, 3, 6, 7, 3, 8, 2, 0}
set02 = {4, 6, 9, 3, 2, 7, 1}

print("Initial set01:", set01)  # Output: {0, 2, 3, 6, 7, 8}
print("Initial set02:", set02)  # Output: {1, 2, 3, 4, 6, 7, 9}

set02.pop()
print("set02 after pop:", set02)  # Output: {2, 3, 4, 6, 7, 9} (or another element removed)

set01.remove(0)
print("set01 after removing '0':", set01)  # Output: {2, 3, 6, 7, 8}

set02.add("AP")
print("set02 after adding 'AP':", set02)  # Output: {2, 3, 4, 6, 7, 9, 'AP'}

set03 = set02.intersection(set01)
print("Intersection of set01 and set02:", set03)  # Output: {2, 3, 6, 7}

set03 = set01.union(set02)
print("Union of set01 and set02:", set03)  # Output: {2, 3, 4, 6, 7, 8, 9, 'AP'}

set03.clear()
print("set03 after clear:", set03)  # Output: set()