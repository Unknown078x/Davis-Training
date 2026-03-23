lst = [{1, 2}, set(), {3, 4}, set()]

result = []

for s in lst:
    if s:          
        result.append(s)


print(result)