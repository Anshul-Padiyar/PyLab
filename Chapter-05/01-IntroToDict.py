dict = {
    "Cpp" : True,          # Boolean
    "JavaScript" : 2.0,    # Float
    "Java" : 3,            # Integer
    "Python" : "Fourth"    # String
}

print(dict, type(dict))
# Output: {'Cpp': True, 'JavaScript': 2.0, 'Java': 3, 'Python': 'Fourth'} <class 'dict'>

print(dict["Cpp"]) # Output: True
print(type(dict["Cpp"])) # Output: <class 'bool'>

print(dict["JavaScript"]) # Output: 2.0
print(type(dict["JavaScript"])) # Output: <class 'float'>

print(dict["Java"]) # Output: 3
print(type(dict["Java"])) # Output: <class 'int'>

print(dict["Python"]) # Output: Fourth
print(type(dict["Python"])) # Output: <class 'str'>