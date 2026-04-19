class WeakPasswordError(Exception):
    pass

try:
    pwd = input("Enter password: ")
    
    if len(pwd) < 8:
        raise WeakPasswordError("Password too short")
    
    if not any(ch.isdigit() for ch in pwd):
        raise WeakPasswordError("Must contain digit")
    
    print("Strong password")

except WeakPasswordError as e:
    print(e)