# Problem statement:
# 1. Smart Student Result Analyzer
# A school stores student data in a file:
#   id,name,marks1,marks2,marks3
# Build a system that:
#       • Reads file
#       • Calculates total, percentage
#       • Assigns grade using selection statements
#       • Handles missing/invalid data using exception handling
#       • Outputs toppers per class 


# Logic:
# create function for checking grades
# open the file in read mode
# fetch the data from the file and convert it into list
# check if length is 5 or not, if not raise error
# fetch the id and name from the list
# add marks to a new list from the fetched list
# sum marks
# calculate percentage
# calculate grades
# add these all as a list into a new list
# get the max percentage from the all students
# find the student that scored the highest percentage
# print it



# function to check the grade using marks percentage
def checkGrade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 40:
        return 'D'
    else:
        return 'F'



# empty list to store the data
students=[]

# opening the file in read mode to get the data 
with open("Classwork/21-04-2026 Questions/students.txt", "r") as file:
    for line in file:
        try:
            data = line.strip().split(",")

            if len(data) != 5:
                raise ValueError("Incomplete data")

            student_id = int(data[0])
            name = data[1]

            # getting the marks
            marks = []
            for m in data[2:]:
                m = m.strip()
                if m == "":
                    raise ValueError("Missing marks")
                marks.append(int(m))

            total = sum(marks)
            percentage = total / len(marks)
            grade = checkGrade(percentage)

            students.append([student_id,name,total,percentage,grade])

        except Exception as e:
            print(f"Skipping invalid record: {line.strip()} | Reason: {e}")

toppers=[]

if students:
    # getting the max percentage throughout the entire students list
    max_percentage = max(s[3] for s in students)

    toppers = []
    for s in students:
        if s[3] == max_percentage:
            toppers.append(s)

    print("\nTopper(s):")
    for t in toppers:
        print(f"{t[1]} with {t[3]:.2f}%")
else:
    print("No valid student data")










# OUTPUT:
# Skipping invalid record: 2,Riya,88,abc,91 | Reason: invalid literal for int() with base 10: 'abc'
# Skipping invalid record: 5,Karan, ,80,85 | Reason: Missing marks

# Topper(s):
# Neha with 95.00%



