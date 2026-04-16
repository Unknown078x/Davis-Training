# Question:7. Reverse File Content Read a file and write its content in reverse order (line-wise) into another file.

# Algorithm:
# Step-1: open the file in read mode
# Step-2: read the content of the file and store it to a variable
# Step-3: reversing the list of lines
# Step-4: opening other file in write mode
# Step-5: reading line by line from the list
# Step-6: writing the lines into the new file


# LOGIC:


with open("Classwork/input1.txt", "r") as file:
    lines = file.readlines()

# reverse the list of lines
lines.reverse()

with open("Classwork/output.txt", "w") as new_file:
    for line in lines:
        new_file.write(line)

print("File reversed successfully.")