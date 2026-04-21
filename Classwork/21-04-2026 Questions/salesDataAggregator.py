# Problem: Sales Data Aggregator
# Given file:
# product,category,price,quantity
# Tasks:
# • Total sales per category
# • Highest selling product
# • Handle invalid rows

# Logic:
# 1. Open the file and read line by line.
# 2. Skip header row.
# 3. Split each line by comma.
# 4. If row doesn't have exactly 4 values → skip (invalid row).
# 5. Convert price and quantity to numbers (handle errors using try-except).
# 6. Calculate total sale = price * quantity.
# 7. Add sales to category total using dictionary.
# 8. Track product with highest total sale.
# 9. Print category totals and highest selling product.

# Code:

file_path = "Classwork/21-04-2026 Questions/sales.txt"

category_sales = {}
product_sales = {}

with open(file_path, "r") as file:
    lines = file.readlines()

    for i in range(len(lines)):
        line = lines[i].strip()
        
        # skip header
        if i == 0:
            continue
        
        parts = line.split(",")
        
        # invalid row check
        if len(parts) != 4:
            continue
        
        product, category, price, quantity = parts
        
        try:
            price = float(price)
            quantity = int(quantity)
        except:
            continue
        
        total = price * quantity
        
        # category total
        if category in category_sales:
            category_sales[category] += total
        else:
            category_sales[category] = total
        
        # product total
        if product in product_sales:
            product_sales[product] += total
        else:
            product_sales[product] = total

# find highest selling product
max_product = None
max_value = 0

for product in product_sales:
    if product_sales[product] > max_value:
        max_value = product_sales[product]
        max_product = product

print("Category Sales:")
for cat, val in category_sales.items():
    print(cat, "->", val)

print("\nHighest Selling Product:")
print(max_product, "->", max_value)


#  Output:

# Category Sales:
# Electronics -> 15000.0
# Grocery -> 8000.0
# Clothing -> 5000.0

# Highest Selling Product:
# Laptop -> 12000.0