# function to check if eligible or not
def check_vote(age):
    return "Eligible" if age >= 18 else "Not Eligible"

# taking age from user
age = int(input("Enter age: "))
# calling the function
print(check_vote(age))