# Question: Remove Duplicate Lines A file contains repeated lines due to logging errors. Create a new file with only unique lines (preserve order).

# Algorithm:
# Step-1: open the file in read mode
# Step-2: open the other file in write mode
# Step-3: take a set to remove duplicacy
# Step-4: read te first file line by line
# Step-5: check if the line is not in the set, if true then write the file into the new file and also add it to the set, in this way only the unique lines will be added to the new files


# LOGIC:

# empty set
seen = set()

# opening file in read mode and other file in write mode
with open("Classwork/input.txt", "r") as file, open("Classwork/output.txt", "w") as new_file:
    # reading file line by line
    for line in file:
        # checking if the file exists in the set or not
        if line not in seen:
            new_file.write(line)
            seen.add(line)

print("Duplicate lines removed.")
