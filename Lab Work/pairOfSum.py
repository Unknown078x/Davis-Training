t = (1, 2, 3, 4, 5)
target = 5

pairs = []
# loop through tuple
for i in range(len(t)):
    
    # check only next elements (avoid duplicates)
    for j in range(i + 1, len(t)):
        
        if t[i] + t[j] == target:
            pairs.append((t[i], t[j]))

print(pairs)