# Question:6. File Merge with Line Numbers You have two files: file1.txt and file2.txt. Merge them into a new file with line numbers.

# Algorithm:
# Step-1: open both the files in read mode
# Step-2: read all the content of the files and save them into some variables 
# Step-3: combine the content of both files and save them to a new variable
# Step-4: open new file in write mode
# Step-5: starting a loop to get the no. of lines
# Step-6: strip the lines to remove extra spaces
# Step-7: writing the data into new file with line number


# LOGIC:


with open("Classwork/file1.txt", "r") as f1, open("Classwork/file2.txt", "r") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

# combine both files
all_lines = lines1 + lines2

with open("Classwork/output.txt", "w") as out:
    for i in range(len(all_lines)):
        line = all_lines[i].strip()
        out.write(str(i+1) + ". " + line + "\n")

print("Files merged with line numbers.")