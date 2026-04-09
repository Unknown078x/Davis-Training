# taking number from user as input
n = int(input("Enter a number:"))
fact = 1

# loop to calculate the factorial of number
for i in range(1, n+1):
    fact *= i

print(fact)