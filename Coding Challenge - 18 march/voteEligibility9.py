# taking age from user
age = int(input("Enter age: "))

# using lambda function
check = lambda x: "Eligible" if x >= 18 else "Not Eligible"
print(check(age))