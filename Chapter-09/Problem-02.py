# 2. Filtering Lines:
    # Write a Python program that asks the user for the name of an input text file and a starting letter.
    # The program should read the input file line by line.
    # For each line, check if the first letter of the line (ignoring leading whitespace) matches the user-provided starting letter.
    # Print only those lines that start with the specified letter.

file_name = input("Enter the name of an input text file : ")
starting_letter = input("Enter a starting letter : ")

with open(file_name) as file :
    file_lines = file.readlines()
    for line in file_lines : 
        line = line.strip(" ")
        if line.lower().startswith(starting_letter.lower()) :
            print(line)