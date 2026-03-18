# recursive function to calculate electricity bill
def calc(u):
    if u == 0:
        return 0
    return 8 + calc(u - 1)

# taking units from user 
units = int(input("Enter units: "))

print("Bill:", calc(units))