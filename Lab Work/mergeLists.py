list1 = [3, 1, 2]
list2 = [2, 4, 5]

# Step 1: Merge both lists
merged = list1 + list2

# Step 2: Remove duplicates using set
unique = set(merged)

# Step 3: Convert back to list and sort
result = list(unique)
result.sort()
print(result)