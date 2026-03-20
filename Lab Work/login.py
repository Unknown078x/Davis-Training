# Function for login system with correct details
def login():
    username = "admin"
    password = "1234"
    
    # counting attempts
    attempts = 0  
    
    # Allowing maximum 3 attempts
    while attempts < 3:
        # Take user input
        user = input("Enter username: ")
        passWrd = input("Enter password: ")
        
        # Validating the credentials
        if user == username and passWrd == password:
            print("Login Successful")
            return  
        
        else:
            attempts += 1
            print(f"Invalid credentials. Try again.\n Attempts left: {3 - attempts}")
    # if loop ends, that means account locked
    else:
        print("Account Locked")


# calling the login function
login()