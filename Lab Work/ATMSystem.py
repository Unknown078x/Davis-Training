# Function to simulate withdrawal system
def withdraw_system():
    # let the current balance be 10000
    balance = 10000  
    
    while True:
        print(f"\nCurrent Balance: {balance}")
        
        # Asking user for withdrawal amount
        amount = float(input("Enter amount to withdraw (or 0 to exit): "))
        # Exit condition
        if amount == 0:
            print("Exiting...")
            break
        
        # Invalid amount check
        if amount < 0:
            print("Invalid amount. Cannot withdraw negative value.")
        
        # Insufficient balance check
        elif amount > balance:
            print("Insufficient balance.")
        
        # Successful withdrawal
        elif amount<balance:
            balance -= amount
            print(f"Withdrawal successful. Remaining balance: {balance}")
        
        else:
            print("Invalid Input")


withdraw_system()