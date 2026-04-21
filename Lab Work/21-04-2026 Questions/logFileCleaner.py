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

# Code:

file_path = "Lab Work/21-04-2026 Questions/log.txt"

unique_logs = set()
error_count = {}

# read file and remove duplicates
with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        unique_logs.add(line)

# filter ERROR logs and count occurrences
for log in unique_logs:
    if "ERROR" in log:
        count = 0
        for line in lines:
            if log == line.strip():
                count += 1
        error_count[log] = count

print("ERROR Log Counts:")
for log, count in error_count.items():
    print(log, "->", count)



# OUTPUT:
# ERROR Log Counts:
# ERROR Failed to load module -> 3
# ERROR Invalid user input -> 2
# ERROR Database connection lost -> 2