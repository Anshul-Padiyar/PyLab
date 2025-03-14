dict = {
    "Cpp" : True,
    "JavaScript" : 2.0,
    "Java" : 3,
    "Python" : "Fourth"
}

print(f"Original dictionary :\n{dict}\n")
# Output: Original dictionary :
# {'Cpp': True, 'JavaScript': 2.0, 'Java': 3, 'Python': 'Fourth'}

print(f"dict.items() :\n{dict.items()}\n")
# Output: dict.items() :
# dict_items([('Cpp', True), ('JavaScript', 2.0), ('Java', 3), ('Python', 'Fourth')])

print(f"dict.keys() :\n{dict.keys()}\n")
# Output: dict.keys() :
# dict_keys(['Cpp', 'JavaScript', 'Java', 'Python'])

print(f"dict.get(\"JavaScript\") :\n{dict.get('JavaScript')}\n")
# Output: dict.get("JavaScript") :
# 2.0

print(f"dict.pop(\"Java\") : \n{dict.pop('Java')}\n")
# Output: dict.pop("Java") :
# 3
print(f"dictionary: \n{dict}\n")
# Output: dictionary:
# {'Cpp': True, 'JavaScript': 2.0, 'Python': 'Fourth'}

print(f"dict.popitem() : \n{dict.popitem()}\n")
# Output: dict.popitem() :
# ('Python', 'Fourth')
print(f"dictionary: \n{dict}\n")
# Output: dictionary:
# {'Cpp': True, 'JavaScript': 2.0}

print(f"dict.clear() :\n{dict.clear()}\n")
# Output: dict.clear() :
# None
print(f"dictionary: \n{dict}\n")
# Output: dictionary:
# {}