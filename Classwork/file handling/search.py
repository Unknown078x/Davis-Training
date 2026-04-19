# Question:8. Keyword Search Tool Ask user for a keyword and return all lines from file containing that keyword.

# Algorithm:
# Step-1: ask the user to give a keyword
# Step-2: open the file in read mode and search for that word in the line
# Step-3: printing the line that contains the same keyword

# LOGIC:


# taking input from user
keyword = input("Enter keyword: ")

# opening file in read mode
with open("Classwork/input3.txt", "r") as file:
    for line in file:
        if keyword in line:
            print(line, end="")
