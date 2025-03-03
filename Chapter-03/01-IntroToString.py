str01 = "God is great!"
str02 = 'God is great!'
str03 = '''God is great!'''

shortstr = str01[0:3]
print(shortstr)  # Output: God

shortstr = str03[-6:-1]
print(shortstr)  # Output: great

# long string
word = "feeling-upset-physically-and-mentally-with-anticipatory-excitement-and-anxiety"

print(len(word))  # Output: 78

# the slice starts at index 9, stops at index 45, and skips every 3rd character
skipword = word[9:45:3]
print(skipword)  # Output: s-piyl-dm

substring = word[:7]
print(substring)  # Output: feeling

substring = word[71:]
print(substring)  # Output: anxiety