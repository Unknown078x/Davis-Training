# Question:10. Compare Two Files Find lines that are present in file1 but not in file2.

# Algorithm:
# Step-1: open the second file in read mode
# Step-2: read the content of the file and store it in a variable
# Step-3: changing into set so that all duplicates are removed
# Step-4: opening first file in read mode
# Step-5: reading the file line by line
# Step-6: checking if the line is not in the second file, if true then print

# LOGIC:




with open("Classwork/file2.txt", "r") as f2:
    lines2 = f2.readlines()

# convert to set for fast lookup
set2 = set(lines2)

with open("Classwork/file1.txt", "r") as f1:
    for line in f1:
        if line not in set2:
            print(line, end="")