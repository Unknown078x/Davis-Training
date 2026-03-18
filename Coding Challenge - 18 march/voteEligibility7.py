# taking age from user
age = int(input("Enter age: "))

# using dictionary mapping
result = {True: "Eligible", False: "Not Eligible"}

# printing eligibility
print(result[age >= 18])