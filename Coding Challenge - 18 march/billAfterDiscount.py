#taking the price from user
price = int(input("Enter price: "))

#taking the discount percentage from the user
discount = int(input("Enter discount percentage: "))

#calculating the discount according the discount percentage and price
discount_amount = (discount / 100) * price

#calculating the final price after discount
final_price = price - discount_amount

#printing the final price after discount
print("Final price after discount:", final_price)