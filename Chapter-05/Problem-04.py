# What will be the length of following set s: 

s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') 
# length of s after these operations? 

print("Final set:", s)  # Output: {20, '20'}
print("Length of set:", len(s))  # Output: 2

# Python considers the integer 1 and the float 1.0 to be equal in value, even though they are of different data types. Therefore, 1 == 1.0 evaluates to True.