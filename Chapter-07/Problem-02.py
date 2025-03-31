# 2. Write a program to greet all the person names stored in a list 'names' and which starts with B.

names = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]
print(f"List of names: {names}")  # Output: List of names: ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot']

for name in names:
    if (name.startswith("B")): 
        print(f"Hello {name}, What's up!") 