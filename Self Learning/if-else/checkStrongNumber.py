# Check strong number (sum of factorial of digits)

import math

num = int(input("Enter number: "))
temp = num
sum_val = 0

while temp:
    sum_val += math.factorial(temp % 10)
    temp //= 10

print("Strong" if sum_val == num else "Not Strong")