# Problem: Bank Transaction Processor
# File contains:
# account,type(deposit/withdraw),amount
# Tasks:
# • Compute final balance
# • Prevent overdraft (raise exception)

# Logic:
# 1. Read file line by line.
# 2. Split each row and validate format.
# 3. Use dictionary:
#    account -> balance
# 4. For each transaction:
#    - If deposit → add amount
#    - If withdraw:
#         check if balance >= amount
#         if not → raise exception (overdraft)
# 5. Handle invalid rows using try-except.
# 6. Print final balances.

# Code:

file_path = "Classwork/21-04-2026 Questions/transactions.txt"

accounts = {}

class OverdraftError(Exception):
    pass

with open(file_path, "r") as file:
    for line in file:
        parts = line.strip().split(",")
        
        # validate row
        if len(parts) != 3:
            continue
        
        acc, t_type, amount = parts
        
        try:
            amount = float(amount)
        except:
            continue
        
        # initialize account
        if acc not in accounts:
            accounts[acc] = 0
        
        try:
            if t_type == "deposit":
                accounts[acc] += amount
            
            elif t_type == "withdraw":
                if accounts[acc] < amount:
                    raise OverdraftError(f"Overdraft in {acc}")
                accounts[acc] -= amount
            
            else:
                continue
        
        except OverdraftError as e:
            print(e)

print("\nFinal Balances:")
for acc, bal in accounts.items():
    print(acc, "->", bal)


# Expected Output (based on sample file below):

# Overdraft in A1

# Final Balances:
# A1 -> 1000.0
# A2 -> 300.0