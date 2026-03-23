# tuple with elements
tup=(1, 2, 2, 3, 1, 4)
# empty dictionary to store frequencies
freq={}

# loop to iterate through the tuple
for i in tup:
    # storing frequency of elements
    freq[i]=tup.count(i)

# printing the result
print(freq)