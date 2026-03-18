# function to calculate the bill after discount
def calculateFinalBill(price,discount):
    return price -  (discount / 100) * price

#taking the price from user
price = int(input("Enter price: "))

#taking the discount percentage from the user
discount = int(input("Enter discount percentage: "))

# calling the function to calculate the bill
print("Final bill after discount: Rs.",calculateFinalBill(price,discount))