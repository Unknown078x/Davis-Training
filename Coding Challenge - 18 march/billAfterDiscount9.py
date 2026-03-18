#taking the price from user
price = int(input("Enter price: "))

#taking the discount percentage from the user
discount = int(input("Enter discount percentage: "))

final = (price * (100 - discount)) // 100
print(final)