#taking the price from user
price = int(input("Enter price: "))

#taking the discount percentage from the user
discount = int(input("Enter discount percentage: "))

#calculating the final price after discount
final_price = price -  (discount / 100) * price

#printing the final price after discount
print("Final price after discount:", final_price)