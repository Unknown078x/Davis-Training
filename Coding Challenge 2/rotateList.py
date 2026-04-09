# list 
nums = [1,2,3]

# take last element and move to front
last = nums[-1]

nums = [last] + nums[:-1]

print(nums)