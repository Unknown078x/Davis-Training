# list 1
a = [1,2,3]
# list 2
b = [2,3,4]

common = []

# loop to iterate through all the elements of both lists
for x in a:
    if x in b and x not in common:
        common.append(x)

print(common)