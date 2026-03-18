# taking units from user
u = int(input("Enter units: "))
bill = 0

while u > 0:
    bill += 8
    u -= 1

print("Electricity Bill:", bill)