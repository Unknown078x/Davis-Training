#taking the price from user
price = float(input("Enter price: "))

#taking the discount percentage from the user
discount = float(input("Enter discount %: "))

final = price * (1 - discount/100)
print(final)