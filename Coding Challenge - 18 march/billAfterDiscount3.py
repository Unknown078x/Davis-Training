#taking the price from user
price = int(input("Enter price: "))

#taking the discount percentage from the user
discount = int(input("Enter discount percentage: "))

#printing the final price after discount
print("Final price after discount:", price -  (discount / 100) * price)