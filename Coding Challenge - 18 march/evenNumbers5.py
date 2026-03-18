# taking input from user
n = int(input("Enter N: "))

# adding evens in a list
evens = [i for i in range(1, n + 1) if i % 2 == 0]
# printing the list
print(evens)