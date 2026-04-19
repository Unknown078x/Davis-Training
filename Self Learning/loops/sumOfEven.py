# Sum of even numbers up to N

n = int(input("Enter limit: "))
sum_val = 0

for i in range(2, n+1, 2):
    sum_val += i

print("Sum:", sum_val)