file = open("Chapter-09/file.txt")
data = file.readlines() 
# readlines(): Returns a list of lines from the file
print(f"data:{data}\ntype of 'data': {type(data)}")
file.close()

file = open("Chapter-09/file.txt")
line01 = file.readline()
# readline(): read the first line of the file "file.txt"
print(line01)
line02 = file.readline()
# Call readline() twice to return both the first and the second line
print(line02)
file.close()