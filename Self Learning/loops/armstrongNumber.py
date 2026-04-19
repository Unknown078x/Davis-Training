# Check Armstrong number

num = int(input("Enter number: "))
temp = num
digits = len(str(num))
sum_val = 0

while temp > 0:
    digit = temp % 10
    sum_val += digit ** digits
    temp //= 10

if sum_val == num:
    print("Armstrong")
else:
    print("Not Armstrong")