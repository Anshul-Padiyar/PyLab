# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up! 

words = {
    'namak': 'Salt',
    'paani': 'Water',
    'kitaab': 'Book',
    'kursi': 'Chair'
}

word = input("Enter the word you want the meaning of: ")

print("The meaning of the word is:", words[word])