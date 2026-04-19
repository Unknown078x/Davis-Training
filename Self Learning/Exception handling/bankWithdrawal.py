class InsufficientBalanceError(Exception):
    pass

balance = 1000

try:
    amt = int(input("Enter amount: "))
    
    if amt > balance:
        raise InsufficientBalanceError("Not enough balance")
    
    balance -= amt
    print("Remaining:", balance)

except ValueError:
    print("Invalid input")
except InsufficientBalanceError as e:
    print(e)