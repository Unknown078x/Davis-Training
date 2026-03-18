# function to check the age
def checkAge(age):
    if age<18:
        return False
    else:
        return True

#taking age from user
age=int(input("Enter your age:"))

# Calling the function to check the age
if checkAge(age):
    print("Eligible")
else:
    print("Not Eligible")