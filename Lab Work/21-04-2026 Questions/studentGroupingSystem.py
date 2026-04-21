# Problem: Student Grouping System
# Given list of students:
# • Group by grade
# • Store in dictionary of lists
# Example:
# A: [students]
# B: [students]

# Logic:
# 1. Use a list of tuples: (name, grade)
# 2. Create empty dictionary:
#    grade -> list of students
# 3. Loop through each student:
#    - If grade not in dictionary → create empty list
#    - Append student name to that grade list
# 4. Print grouped data

# Code:

students = [
    ("Aman", "A"),
    ("Riya", "B"),
    ("Karan", "A"),
    ("Neha", "C"),
    ("Raj", "B"),
    ("Simran", "A")
]

grouped = {}

for name, grade in students:
    if grade not in grouped:
        grouped[grade] = []
    
    grouped[grade].append(name)

print("Grouped Students:")
for grade, names in grouped.items():
    print(grade, "->", names)


# Expected Output:

# Grouped Students:
# A -> ['Aman', 'Karan', 'Simran']
# B -> ['Riya', 'Raj']
# C -> ['Neha']