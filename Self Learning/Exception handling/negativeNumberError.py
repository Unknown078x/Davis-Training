class NegativeNumberError(Exception):
    pass

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    
    if a < 0 or b < 0:
        raise NegativeNumberError("Negative values not allowed")
    
    print(a / b)

except NegativeNumberError as e:
    print(e)
except ZeroDivisionError:
    print("Cannot divide by zero")