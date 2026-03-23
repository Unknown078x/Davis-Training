# Original list
lst = [10, 20, 30, 40, 50]

# Number of positions to rotate
k = 2

# Length of list
n = len(lst)

# Handle case where k is greater than list size
k = k % n

# Take last k elements from the list
last_part = lst[-k:]


# Take remaining elements from start to n-k
first_part = lst[:-k]

# Combine both parts to get rotated list
rotated = last_part + first_part

# Output result
print(rotated)