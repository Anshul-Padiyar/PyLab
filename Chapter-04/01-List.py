list01 = ["Apple", "Banana", 3.14, 2902, True, "Sherya", "Arjun"]
print(list01)  # Output: ['Apple', 'Banana', 3.14, 2902, True, 'Sherya', 'Arjun']

print(list01[2])  # Output: 3.14

# modify the second element of the list
list01[1] = "Samsung"
print(list01)  # Output: ['Apple', 'Samsung', 3.14, 2902, True, 'Sherya', 'Arjun']

# list slicing
print(list01[2:5])  # Output: [3.14, 2902, True]