# let the list of numbers
nums = [10,60,30,80]

count = 0
# loop to iterate through the list of the elements and count how many elements are greater than 50
for n in nums:
    if n > 50:
        count += 1

# printing the count of numbers greater than 50
print(count)