try:
    n = int(input("Enter number: "))
    print("Square:", n*n)

except ValueError:
    print("Invalid integer input")