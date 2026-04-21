# Problem: Inventory Management System
# Features:
# • Add/update/delete items
# • Store in dictionary
# • Save/load from file

# Logic:
# 1. Use a dictionary:
#    item_name -> quantity
# 2. Load existing data from file (if file exists).
# 3. Show menu:
#    1. Add/Update item
#    2. Delete item
#    3. View inventory
#    4. Save to file
#    5. Exit
# 4. For add/update:
#    - If item exists → update quantity
#    - Else → add new item
# 5. For delete:
#    - Remove item if exists
# 6. Save dictionary to file (item,quantity format)
# 7. Keep program simple using loops + conditions

# Code:

file_path = "Classwork/21-04-2026 Questions/inventory.txt"
inventory = {}

# load from file
try:
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(",")
                if len(parts) == 2:
                    item, qty = parts
                    inventory[item] = int(qty)
except:
    pass  # file may not exist initially

while True:
    print("\n1. Add/Update Item")
    print("2. Delete Item")
    print("3. View Inventory")
    print("4. Save to File")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        
        inventory[item] = qty
        print("Item added/updated.")

    elif choice == "2":
        item = input("Enter item to delete: ")
        
        if item in inventory:
            del inventory[item]
            print("Item deleted.")
        else:
            print("Item not found.")

    elif choice == "3":
        print("\nInventory:")
        for item in inventory:
            print(item, "->", inventory[item])

    elif choice == "4":
        with open(file_path, "w") as file:
            for item in inventory:
                file.write(item + "," + str(inventory[item]) + "\n")
        print("Data saved to file.")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")


# Output:

# 1. Add/Update Item
# 2. Delete Item
# 3. View Inventory
# 4. Save to File
# 5. Exit
# Enter choice: 1
# Enter item name: Laptop
# Enter quantity: 5
# Item added/updated.

# Enter choice: 3
# Inventory:
# Laptop -> 5

# Enter choice: 4
# Data saved to file.

# Enter choice: 5
# Exiting...