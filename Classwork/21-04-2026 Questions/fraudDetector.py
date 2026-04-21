# Problem: Fraud Transaction Detector
# Given a list of transactions:
# • Detect suspicious ones based on:
#   - Amount > threshold
#   - Same user multiple transactions within short time 


# use:
# • loops + conditions
# • Store flagged data in dictionary

# Logic:
# 1. Loop through each transaction.
# 2. If amount > threshold → mark as suspicious.
# 3. Track last transaction time of each user using a dictionary.
# 4. If same user makes another transaction within short time → mark suspicious.
# 5. Store all suspicious transactions in a dictionary (user as key).

# Code:

transactions = [
    ("user1", 5000, 1),
    ("user2", 200, 2),
    ("user1", 300, 3),
    ("user3", 7000, 4),
    ("user1", 100, 4)
]

threshold = 1000
time_limit = 2  # short time gap

last_time = {}
fraud = {}

for user, amount, time in transactions:
    
    # condition 1: amount exceeds threshold
    if amount > threshold:
        if user not in fraud:
            fraud[user] = []
        fraud[user].append((amount, time))
    
    # condition 2: multiple transactions in short time
    if user in last_time:
        if time - last_time[user] <= time_limit:
            if user not in fraud:
                fraud[user] = []
            fraud[user].append((amount, time))
    
    # update last transaction time
    last_time[user] = time

print("Suspicious Transactions:")
print(fraud)




# OUTPUT:
# Suspicious Transactions:
# {'user1': [(5000, 1), (300, 3), (100, 4)], 'user3': [(7000, 4)]}