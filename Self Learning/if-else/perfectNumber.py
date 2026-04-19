# Check perfect number

num = int(input("Enter number: "))
sum_val = 0

for i in range(1, num):
    if num % i == 0:
        sum_val += i

print("Perfect" if sum_val == num else "Not Perfect")