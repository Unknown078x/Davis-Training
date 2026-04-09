# list
nums = [10,20,5,15]

largest = second = -999999

# loop to iterate through all the elements
for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print("Second largest:", second)