# taking list of elements
nums = [1,1,2,3]

result = []

# loop to iterate through all the elements of the list
for n in nums:
    # add only if not already present
    if n not in result:
        result.append(n)

print(result)