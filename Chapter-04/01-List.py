l1 = ["Apple", "Banana", 3.14, 2902, True, "Sherya", "Arjun"]
print(l1)  # Output: ['Apple', 'Banana', 3.14, 2902, True, 'Sherya', 'Arjun']

print(l1[2])  # Output: 3.14

# modify the second element of the list
l1[1] = "Samsung"
print(l1)  # Output: ['Apple', 'Samsung', 3.14, 2902, True, 'Sherya', 'Arjun']

# list slicing
print(l1[2:5])  # Output: [3.14, 2902, True]