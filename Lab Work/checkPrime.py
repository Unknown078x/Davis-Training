# Function to check if a number is prime or not
def is_prime(n):
    
    # Prime numbers are greater than 1
    if n <= 1:
        return False
    
    # Check divisibility from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False   
    
    # if not divisors found that means the number is prime 
    return True  


# Taking input from user
num = int(input("Enter a number: "))

# Use if-else to display result
if is_prime(num):
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is not a Prime Number")