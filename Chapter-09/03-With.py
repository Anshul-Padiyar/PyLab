with open("Chapter-09/file.txt", "a+") as file:
    file.write("Open the file in read mode using 'with', which automatically closes the file\n")
    file.seek(0)        # Moving cursor to beginning of file...
    print(file.read())