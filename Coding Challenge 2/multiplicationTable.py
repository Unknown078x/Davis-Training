# taking the number whose table has to be printed
n = int(input("Enter a number:"))

# loop to print the multiplication table
for i in range(1, 11):
    print(n * i, end=" ")