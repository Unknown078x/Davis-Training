# taking input from user 
n = int(input("Enter a number"))
# storing the actual number 
temp = n
rev = 0

# loop to iterate through the each digit of the number
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

# checking if the actual and reversed number are same or not
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")