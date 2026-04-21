# Problem: Error Log Reporter
# Read error logs:
# • Group by error type
# • Count occurrences
# • Write summary file

# Logic:
# 1. Read log file line by line.
# 2. For each line:
#    - Extract error type (assume format: TYPE: message)
# 3. Use dictionary:
#    error_type -> count
# 4. Increment count for each occurrence.
# 5. Write summary to a new file in format:
#    TYPE -> count

# Code:

input_file = "Lab Work/21-04-2026 Questions/error_log.txt"
output_file = "Lab Work/21-04-2026 Questions/summary.txt"

error_count = {}

with open(input_file, "r") as file:
    for line in file:
        line = line.strip()
        
        if ":" in line:
            error_type = line.split(":")[0]
            
            if error_type in error_count:
                error_count[error_type] += 1
            else:
                error_count[error_type] = 1

# write summary
with open(output_file, "w") as file:
    for err, count in error_count.items():
        file.write(err + " -> " + str(count) + "\n")

print("Summary written to", output_file)


# Expected Output (based on sample file below):

# summary.txt:
# ERROR -> 3
# WARNING -> 2
# INFO -> 1