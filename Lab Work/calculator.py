# calculator function
def calculator():
    
    # loop until user exits
    while True:
        print("\n--- Calculator Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        # taking choice from user
        choice = input("Enter your choice (1-5): ")
        
        # checking if user exits 
        if choice == "5":
            print("Exiting calculator...")
            break
        
        # checking if user gives invalid choice
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice")
            input("Press Enter to continue...")  # pause
            continue
        
        # taking numbers from user
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        # checking the choices
        if choice == "1":
            result = a + b
        elif choice == "2":
            result = a - b
        elif choice == "3":
            result = a * b
        elif choice == "4":
            if b == 0:
                result = "Error: Division by zero"
            else:
                result = a / b
        
        # printing the result
        print("Result:", result)
        
        # THIS is what you were missing
        input("\nPress Enter to continue...")

calculator()