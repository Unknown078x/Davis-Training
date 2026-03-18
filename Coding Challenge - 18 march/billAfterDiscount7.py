#taking the price from user
price = float(input("Enter price: "))

#taking the discount percentage from the user
discount = float(input("Enter discount %: "))

# lambda function to calculate the bill after discount
calc = lambda p, d: p - (p * d / 100)

print("Bill after discount:",calc)