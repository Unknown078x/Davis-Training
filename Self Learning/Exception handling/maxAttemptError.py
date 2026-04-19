class MaxAttemptsError(Exception):
    pass

attempts = 3

for i in range(attempts):
    try:
        n = int(input("Enter number: "))
        print("Valid input:", n)
        break
    except ValueError:
        print("Invalid input")
else:
    raise MaxAttemptsError("Too many invalid attempts")