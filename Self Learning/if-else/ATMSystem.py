# ATM simulation

balance = 10000
amount = int(input("Enter amount: "))

if amount <= balance:
    if amount % 100 == 0:
        print("Withdraw successful")
    else:
        print("Enter multiple of 100")
else:
    print("Insufficient balance")