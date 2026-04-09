# list of elements
nums = [1,2,2,3]

# dictionary to store frequency of each element of the list
freq = {}

for n in nums:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1

print(freq)