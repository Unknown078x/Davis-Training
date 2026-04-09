# taking number from user as input
n = int(input("Enter a number:"))
s = 0

# calculating the sum of the digits
while n > 0:
    s += n % 10
    n //= 10

print(s)