# Function to calculate grade based on marks percentage
def calculate_grade(marks):
    # Checking if marks percentage is in valid range or not
    if marks < 0 or marks > 100:
        return "Invalid Marks"
    
    # checking the grades according to the marks percentage
    if marks >= 90:
        return "Grade A"
    elif marks >= 75:
        return "Grade B"
    elif marks >= 50:
        return "Grade C"
    else:
        return "Fail"


# Loop to process marks of 5 students
for i in range(1, 6):
    # Taking input from user
    marks = float(input(f"Enter marks Percentage for student {i}: "))
    
    # Calling the function to get the grades
    grade = calculate_grade(marks)
    
    # Displaying result
    print(f"Student {i} got : {grade}")