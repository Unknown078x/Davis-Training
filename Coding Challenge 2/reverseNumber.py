# taking number from user as input 
n = int(input("Enter a number"))
rev = 0
# loop to iterate through the each digit of the number
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

print(rev)