# problem statement:
# 4. Custom Password Validator
# Rules:
# • Min 8 chars
# • At least 1 uppercase, 1 lowercase, 1 digit
# Use:
# • string operations
# • loops + conditionals
# • Raise custom exception if invalid


# Logic:
# create invalid password error exception 
# create function to validate password
# check if the length of password is less than 8
# check if password has uppercase character, lowercase character and has digit or not
# if password doesn't have any of the above, raise custom exception
# if password contains everything, return true
# call the function after taking input from user



class InvalidPasswordError(Exception):
    pass

# function to validate the password 
def validatePassword(password):
    if len(password) < 8:
        raise InvalidPasswordError("Password must be at least 8 characters long")

    isUpper = False
    isLower = False
    hasDigit = False

    for ch in password:
        if ch.isupper():
            isUpper = True
        elif ch.islower():
            isLower = True
        elif ch.isdigit():
            hasDigit = True

    if not isUpper:
        raise InvalidPasswordError("Password must contain at least one uppercase letter")

    if not isLower:
        raise InvalidPasswordError("Password must contain at least one lowercase letter")

    if not hasDigit:
        raise InvalidPasswordError("Password must contain at least one digit")

    return True


try:
    pwd = input("Enter password: ")
    if validatePassword(pwd):
        print("Valid password ✅")
except InvalidPasswordError as e:
    print("Invalid password ❌:", e)







# OUTPUT:
# Enter password: Hello111
# Valid password ✅