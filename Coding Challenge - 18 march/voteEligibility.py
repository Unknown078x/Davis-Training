#taking age from user
age=int(input("Enter your age:"))

#checking the age criteria
if age<18:
    print("Not Eligible")
elif(age<0 or age>100):
    print("Enter valid age")
else:
    print("Eligible")