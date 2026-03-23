l1 = [1, 2, 3]
l2 = [2, 3, 4]
l3 = [2, 5, 3]


# Convert lists to sets and find intersection
result = list(set(l1) & set(l2) & set(l3))

print(result)