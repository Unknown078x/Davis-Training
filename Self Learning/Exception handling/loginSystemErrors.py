class UserNotFoundError(Exception):
    pass

class WrongPasswordError(Exception):
    pass

try:
    user = input("Username: ")
    pwd = input("Password: ")
    
    if user != "admin":
        raise UserNotFoundError("User not found")
    
    if pwd != "1234":
        raise WrongPasswordError("Wrong password")
    
    print("Login successful")

except UserNotFoundError as e:
    print(e)
except WrongPasswordError as e:
    print(e)