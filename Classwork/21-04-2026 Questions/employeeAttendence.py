# Problem: Employee Attendance Tracker
# File contains:
# emp_id,date,status
# Tasks:
# • Count present/absent days
# • Detect employees with low attendance (<75%)

# Logic:
# 1. Open file and read all lines.
# 2. Skip header.
# 3. For each row:
#    - Split by comma
#    - Validate row length
# 4. Use dictionary to track:
#    emp_id -> [present_count, total_days]
# 5. If status == "P" → increment present
#    else count as absent (but still increase total days)
# 6. After processing:
#    attendance % = (present / total_days) * 100
# 7. Print counts and identify employees with <75%

# Code:

file_path = "Classwork/21-04-2026 Questions/attendance.txt"

attendance = {}

with open(file_path, "r") as file:
    lines = file.readlines()
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # skip header
        if i == 0:
            continue
        
        parts = line.split(",")
        
        # invalid row check
        if len(parts) != 3:
            continue
        
        emp_id, date, status = parts
        
        if emp_id not in attendance:
            attendance[emp_id] = [0, 0]  # [present, total]
        
        # total days
        attendance[emp_id][1] += 1
        
        # present count
        if status == "P":
            attendance[emp_id][0] += 1

print("Attendance Summary:")
low_attendance = []

for emp in attendance:
    present, total = attendance[emp]
    percent = (present / total) * 100
    
    print(emp, "-> Present:", present, "Absent:", total - present, "(", round(percent, 2), "% )")
    
    if percent < 75:
        low_attendance.append(emp)

print("\nEmployees with Low Attendance (<75%):")
for emp in low_attendance:
    print(emp)


# Output:

# Attendance Summary:
# E1 -> Present: 3 Absent: 1 ( 75.0 % )
# E2 -> Present: 1 Absent: 3 ( 25.0 % )
# E3 -> Present: 2 Absent: 0 ( 100.0 % )

# Employees with Low Attendance (<75%):
# E2