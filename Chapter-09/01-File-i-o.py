# Read the file
file = open("Chapter-09/file.txt", "r")
data = file.read()
print(data)
file.close()

# Write the file
file = open("Chapter-09/file.txt", "w")
file.write("In order to write to a file, we first open it in write or append mode after which, we use the python's f.write() method to write to the file!")
file.close()