# Function to check palindrome
def is_palindrome(value):
    
    # Convert input to string
    value = str(value)
    
    reversed_value = ""
    
    # Use loop to reverse the string
    for ch in value:
        reversed_value = ch + reversed_value
    
    # Compare original and reversed
    if value == reversed_value:
        print(f"{value} is Palindrome")
    else:
        print(f"{value} is Not a Palindrome")


# Take input from user
data = input("Enter a number or string: ")

# Call function
is_palindrome(data)