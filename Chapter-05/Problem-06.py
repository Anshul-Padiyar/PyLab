# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique. 

d = {}

name = input("Enter a friend name : ")  # Enter a friend name : Alpha
lang = input("Enter a language : ")     # Enter a language : Python
d.update({name : lang})

name = input("Enter a friend name : ")  # Enter a friend name : Beta
lang = input("Enter a language : ")     # Enter a language : Java
d.update({name : lang})

name = input("Enter a friend name : ")  # Enter a friend name : Charlie
lang = input("Enter a language : ")     # Enter a language : C++
d.update({name : lang})

name = input("Enter a friend name : ")  # Enter a friend name : Deta
lang = input("Enter a language : ")     # Enter a language : JavaScript
d.update({name : lang})

print(d)  # {'Alpha': 'Python', 'Beta': 'Java', 'Charlie': 'C++', 'Deta': 'JavaScript'}