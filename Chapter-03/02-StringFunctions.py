string = "God is great!"

print(len(string))  # Output: 13

print(string.startswith("God"))  # Output: True

print(string.endswith("great"))  # Output: False

print(string.count("g"))  # Output: 1

print(string.index("g"))  # Output: 6

print(string.capitalize())  # Output: God is great!

print(string.lower())  # Output: god is great!

print(string.upper())  # Output: GOD IS GREAT!

print(string.replace("great", "cool"))  # Output: God is cool!

print(string.find("great"))  # Output: 7