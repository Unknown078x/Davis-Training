# taking input from user 
n = int(input("Enter N: "))

# creating list with filter and lambda function with condition
evens = list(map(lambda x: x if x % 2 == 0 else None, range(1, n + 1)))

# printing the even numbers
print([i for i in evens if i is not None])