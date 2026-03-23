nested = [[1, 2], [3, 4], [5]]

flat = []

# outer list pe loop
for sublist in nested:
    # inner list ke elements pe loop
    for num in sublist:
        flat.append(num)

print(flat)