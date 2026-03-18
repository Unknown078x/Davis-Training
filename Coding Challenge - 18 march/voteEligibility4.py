#taking age from user
age=int(input("Enter your age:"))

while age<100 and age>0:
    if age<18:
        print("Not Eligible")
        age=0
    else:
        print("Eligible")
        age=0

    