# taking marks from the user
marks = int(input("Enter marks:"))

# printing grades according to marks
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")