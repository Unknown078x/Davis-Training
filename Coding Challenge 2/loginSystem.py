# taking username from user
user = input("Username: ")
# taking password from user
pwd = input("Password: ")

# checking if password and username is valid
if user == "admin" and pwd == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")