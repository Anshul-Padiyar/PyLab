#3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.

for table in range(2, 21) :
    with open(f"Chapter-09/Tables/multiplication_table_of_{table}.txt", "w+") as file :
        file.write(f"Multiplication table of {table} :\n")
        for i in range(1, 11) :
            file.write(f"{table}\tx\t{i}\t=\t{table*i}\n")
        print(f"File of multiplaction table '{table}' has created...\n")