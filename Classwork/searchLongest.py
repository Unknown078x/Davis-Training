# Question:9. Find Longest Line Identify the longest line in a file and print its length and content.

# Algorithm:
# Step-1: open the file in read mode
# Step-2: let the max line and max length be initialized with none and zero
# Step-3: reading he file line by line
# Step-4: adding the line into list by using the strip method
# Step-5: checking if the line is greater than max length or not, if true then interchange the length and line
# Step-6: printing the longest length and longest line


# LOGIC:


max_line = None
max_length = 0

with open("Classwork/input4.txt", "r") as file:
    for line in file:
        clean_line = line.strip()
        
        if len(clean_line) > max_length:
            max_length = len(clean_line)
            max_line = clean_line

if max_line is None:
    print("File is empty")
else:
    print("Longest line length:", max_length)
    print("Longest line:", max_line)