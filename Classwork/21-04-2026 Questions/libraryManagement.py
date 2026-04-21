# Problem: Library Management System (Basic)
# Features:
# • Issue/return books
# • Track availability
# • Store records in file

# Logic:
# 1. Use dictionary:
#    book_name -> [total_copies, available_copies]
# 2. Load data from file if exists.
# 3. Menu:
#    1. Issue book
#    2. Return book
#    3. View books
#    4. Save to file
#    5. Exit
# 4. Issue:
#    - Check if book exists and available > 0
#    - Reduce available count
# 5. Return:
#    - Increase available count (but not beyond total)
# 6. Save all data to file
# 7. Keep everything simple using loops + conditions

# Code:

file_path = "Classwork/21-04-2026 Questions/library.txt"
library = {}

# load from file
try:
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(",")
                if len(parts) == 3:
                    book, total, available = parts
                    library[book] = [int(total), int(available)]
except:
    pass

while True:
    print("\n1. Issue Book")
    print("2. Return Book")
    print("3. View Books")
    print("4. Save to File")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        
        if book in library:
            if library[book][1] > 0:
                library[book][1] -= 1
                print("Book issued.")
            else:
                print("Book not available.")
        else:
            print("Book not found.")

    elif choice == "2":
        book = input("Enter book name: ")
        
        if book in library:
            if library[book][1] < library[book][0]:
                library[book][1] += 1
                print("Book returned.")
            else:
                print("All copies already in library.")
        else:
            print("Book not found.")

    elif choice == "3":
        print("\nLibrary Records:")
        for book in library:
            total, available = library[book]
            print(book, "-> Total:", total, "Available:", available)

    elif choice == "4":
        with open(file_path, "w") as file:
            for book in library:
                total, available = library[book]
                file.write(book + "," + str(total) + "," + str(available) + "\n")
        print("Data saved.")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")


# Expected Output (sample interaction):

# 1. Issue Book
# 2. Return Book
# 3. View Books
# 4. Save to File
# 5. Exit
# Enter choice: 3
# Library Records:
# Python Basics -> Total: 5 Available: 3
# Data Structures -> Total: 4 Available: 4

# Enter choice: 1
# Enter book name: Python Basics
# Book issued.

# Enter choice: 3
# Library Records:
# Python Basics -> Total: 5 Available: 2