# taking units from user
units = int(input("Enter units: "))

bill = sum([8 for _ in range(units)])
print("Bill:", bill)