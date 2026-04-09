# dictionary
data = {"b":2,"a":1}

sorted_dict = {}

for key in sorted(data):
    sorted_dict[key] = data[key]

print(sorted_dict)