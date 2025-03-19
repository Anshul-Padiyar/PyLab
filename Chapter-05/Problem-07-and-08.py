# Problem-06: Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique. 
# Problem-07: If the names of 2 friends are same; what will happen to the program in Problem-06? 
# Problem-08: If languages of two friends are same; what will happen to the program in Problem-06? 

d = {}

name = input("Enter a friend name : ")      # Alpha             # Alpha
lang = input("Enter a language : ")             # Python            # Python
d.update({name : lang})

name = input("Enter a friend name : ")      # Beta              # Beta
lang = input("Enter a language : ")             # Java              # Java
d.update({name : lang})

name = input("Enter a friend name : ")      # Charlie           # Charlie
lang = input("Enter a language : ")             # C++               # Python
d.update({name : lang})

name = input("Enter a friend name : ")      # Charlie           #Deta
lang = input("Enter a language : ")             # JavaScript        #JavaScript
d.update({name : lang})

print("If the names of 2 friends are same : ", d) # {'Alpha': 'Python', 'Beta': 'Java', 'Charlie': 'JavaScript'}
# If names are the same, the last entry will overwrite the previous one with the same name

print("If languages of two friends are same : ", d) # {'Alpha': 'Python', 'Beta': 'Java', 'Charlie': 'Python', 'Deta': 'JavaScript'}
# If languages are the same, it does not affect the dictionary since keys (names) are unique