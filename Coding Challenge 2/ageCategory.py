# taking age input from user
age = int(input("Enter age: "))

# checking the age category
if age < 18:
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior")