nums = [10, 0, 5]

for n in nums:
    try:
        print(100 / n)
    except ZeroDivisionError:
        print("Cannot divide by zero")