# Program to print triangle pattern
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    
    # Check if row is even or odd
    if i % 2 == 0:
        symbol = "*"
    else:
        symbol = "#"
    
    # Print the pattern for that row
    for j in range(i):
        print(symbol, end=" ")
    
    # Move to next line after each row
    print()