# Question:12. Tail Implementation (Like Linux tail) Display last N lines of a file efficiently.

# Algorithm:
# Step-1: asking user how many lines he/she want to read
# Step-2: opening file in read mode
# Step-3: reading the content of the file and saving it into a variable
# Step-4: printing the last n lines from the content using for loop

# LOGIC:

# taking input from user of number of lines
n = int(input("Enter number of lines: "))

with open("input.txt", "r") as file:
    lines = file.readlines()

# printing last n lines
for line in lines[-n:]:
    print(line, end="")