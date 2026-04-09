marks = {"A":80,"B":95,"C":78}

top_student = ""
max_marks = -1

for student in marks:
    if marks[student] > max_marks:
        max_marks = marks[student]
        top_student = student

print(top_student)