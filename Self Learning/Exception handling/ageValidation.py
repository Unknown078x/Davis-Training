class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120")
    
    print("Valid age")

except ValueError:
    print("Enter valid number")
except InvalidAgeError as e:
    print(e)