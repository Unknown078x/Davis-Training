# list of elements
nums = [5,8,2]

# let the first element to be the max
max_val = nums[0]

# loop to iterate through the list to get the max
for n in nums:
    if n > max_val:
        max_val = n

print(max_val)