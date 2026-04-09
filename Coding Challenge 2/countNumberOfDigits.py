# taking number from user
n = int(input("Enter a number:"))
count = 0

# loop to count the number of digits
while n > 0:
    count += 1
    n //= 10

print(count)