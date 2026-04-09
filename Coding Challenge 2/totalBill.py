# function to calculate total bill 
def total_bill(items):
    total = 0

    for price in items:
        total += price

    return total

print(total_bill([100,200,300]))