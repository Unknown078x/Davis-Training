#function to calculate the bill
def calculateBill(units):
    return 8*units

#taking input of units consumed by the user
units=int(input("Enter the units consumed:"))

# calling the function to print the electricity bill
print("Total bill: Rs.",calculateBill(units))