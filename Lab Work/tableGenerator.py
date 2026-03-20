# Function to print multiplication table
def print_table(num):
    
    # Restrict negative input using if
    if num < 0:
        print("Negative numbers are not allowed")
        return       
    # Print table from 1 to 10 using for loop
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


# Take input from user
num = int(input("Enter a number: "))
# Call the function
print_table(num)