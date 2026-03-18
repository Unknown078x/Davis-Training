# function to check the age
def checkAge(age):
    if age>100 or age<0:
        return "Input Valid Age"
    elif age<18:
        return "Not Eligible"
    else:
        return "Eligible"

#taking age from user
age=int(input("Enter your age:"))

# Calling the function to check the age
print(checkAge(age))


