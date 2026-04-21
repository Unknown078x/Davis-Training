# Problem: Marks Improvement Tracker
# Compare two exam files:
# • Identify students who improved
# • Calculate improvement %

# Logic:
# 1. Read both files (exam1.txt and exam2.txt).
# 2. Store data in dictionaries:
#    roll_no -> marks
# 3. Loop through students in exam1:
#    - If student exists in exam2:
#        compare marks
#        if marks increased → calculate improvement %
# 4. Improvement % = ((new - old) / old) * 100
# 5. Store improved students in dictionary.
# 6. Print results.

# Code:

file1 = "Lab Work/21-04-2026 Questions/exam1.txt"
file2 = "Lab Work/21-04-2026 Questions/exam2.txt"

exam1 = {}
exam2 = {}

# read exam1
with open(file1, "r") as f:
    for line in f:
        parts = line.strip().split(",")
        if len(parts) == 2:
            roll, marks = parts
            try:
                exam1[roll] = float(marks)
            except:
                continue

# read exam2
with open(file2, "r") as f:
    for line in f:
        parts = line.strip().split(",")
        if len(parts) == 2:
            roll, marks = parts
            try:
                exam2[roll] = float(marks)
            except:
                continue

# compare and find improvement
improved = {}

for roll in exam1:
    if roll in exam2:
        old = exam1[roll]
        new = exam2[roll]
        
        if new > old and old != 0:
            percent = ((new - old) / old) * 100
            improved[roll] = round(percent, 2)

print("Students who improved:")
for roll in improved:
    print(roll, "->", improved[roll], "%")


# Expected Output (based on sample files below):

# Students who improved:
# S1 -> 20.0 %
# S3 -> 25.0 %