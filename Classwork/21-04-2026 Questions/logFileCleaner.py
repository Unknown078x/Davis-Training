# Problem: Log File Cleaner
# Given a log file:
# • Remove duplicate entries
# • Filter only ERROR logs
# • Count occurrences

# Use:
# • set for uniqueness
# • file handling

# Logic:
# 1. Open the file and read line by line.
# 2. Use a set to remove duplicate lines.
# 3. From unique lines, keep only those containing "ERROR".
# 4. Count how many times each ERROR line appears in original file.
# 5. Store result in a dictionary and print.


# code:


# file path 
file_path = "Classwork/21-04-2026 Questions/log.txt"

error_count = {}

# opening file in read mode
with open(file_path, "r") as file:
    # reading all lines and storing them to a list
    lines = file.readlines()
    if len(lines)>0:
        unique_logs=set(lines)

# loop on original lines
for line in lines:
    # cleaning lines (removing extra spaces)
    line = line.strip()
    
    # checking if any line have exactly [ERROR] 
    if " [ERROR] " in line:
        # checking if the error already exists in the dictionary or not
        if line in error_count:
            #increasing the count of the error by 1
            error_count[line] += 1
        else:
            # if the error is first time, then initialize it by 1
            error_count[line] = 1

# printing output
print("ERROR Log Counts:\n")

#printing log and count from the dictionary
for log, count in error_count.items():
    # printing the log message and its count
    print(log, "->", count)

# OUTPUT:
# ERROR Log Counts:
# ERROR Failed to load module -> 3
# ERROR Invalid user input -> 2
# ERROR Database connection lost -> 2