# taking age from user
age = int(input("Enter age: "))

# if true, stored in boolean is_eligible
is_eligible = age >= 18
if is_eligible:
    print("Eligible")
else:
    print("Not Eligible")