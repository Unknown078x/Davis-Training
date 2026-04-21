# Problem: Quiz System
# Features:
# • Load questions from file
# • Ask user
# • Score calculation
# • Handle invalid input

# Logic:
# 1. Read questions from file (format: question,option1,option2,option3,option4,correct_option_number)
# 2. Store each question as a list.
# 3. Loop through questions:
#    - Display question and options
#    - Take user input
#    - Validate input (must be 1-4)
#    - Compare with correct answer
#    - Update score
# 4. At end, print final score.

# Code:

file_path = "Classwork/21-04-2026 Questions/quiz.txt"

questions = []

# load questions
with open(file_path, "r") as file:
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 6:
            questions.append(parts)

score = 0
total = len(questions)

for q in questions:
    question = q[0]
    options = q[1:5]
    correct = q[5]
    
    print("\n" + question)
    for i in range(4):
        print(i+1, ".", options[i])
    
    while True:
        ans = input("Enter option (1-4): ")
        
        if ans in ["1", "2", "3", "4"]:
            break
        else:
            print("Invalid input. Try again.")
    
    if ans == correct:
        score += 1

print("\nFinal Score:", score, "/", total)


# Expected Output (sample run):

# What is 2+2?
# 1. 3
# 2. 4
# 3. 5
# 4. 6
# Enter option (1-4): 2

# What is capital of India?
# 1. Mumbai
# 2. Delhi
# 3. Kolkata
# 4. Chennai
# Enter option (1-4): 2

# Final Score: 2 / 2