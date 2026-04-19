# Find maximum element in a list

nums = [10, 45, 2, 99, 23]

max_val = nums[0]

for num in nums:
    if num > max_val:
        max_val = num

print("Max value:", max_val)