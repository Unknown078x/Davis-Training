# taking input from user
n = int(input("Enter N: "))
# using filter with lambda function to create a list 
evens = list(filter(lambda x: x % 2 == 0, range(1, n + 1)))

# printing the list
print(evens)