#taking the price from user
price = float(input("Enter price: "))

#taking the discount percentage from the user
discount = float(input("Enter discount %: "))

#calculating the discount according the discount percentage and price
final_price = price - (price * discount / 100)


print("Final price after discount",final_price)