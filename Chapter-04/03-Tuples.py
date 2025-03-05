tuple01 = ("Apple", "Banana")
print(tuple01[0])  # Output: Apple

tuple02 = (3.14, 2902, True)
tuple03 = ("Sherya", "Arjun")

# concatenate tuples
tuple04 = tuple01 + tuple02 + tuple03
print(tuple04)  # Output: ('Apple', 'Banana', 3.14, 2902, True, 'Sherya', 'Arjun')

tuple05 = (78, 45, 23, 89, 23)
print(tuple05.count(23))  # Output: 2 (23 appears twice in the tuple)
print(tuple05.index(45))  # Output: 1 (45 is at index 1)

tuple06 = (1)
print(type(tuple06))  # Output: <class 'int'>

tuple07 = (1,)
print(type(tuple07))  # Output: <class 'tuple'>

tuple08 = () # empty tuple