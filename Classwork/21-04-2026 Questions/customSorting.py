# Problem: Custom Sorting Engine
# Sort list of tuples:
# (name, marks, age)
# Sort by:
# • marks desc
# • age asc
# Without using built-in sorted() (implement logic manually)

# Logic:
# 1. Use a simple sorting algorithm (Bubble Sort).
# 2. Compare adjacent elements:
#    - If marks of first < marks of second → swap (for descending)
#    - If marks equal:
#         if age of first > age of second → swap (for ascending age)
# 3. Repeat passes until list is sorted.
# 4. Print final sorted list.

# Code:

data = [
    ("Aman", 85, 20),
    ("Riya", 90, 22),
    ("Karan", 85, 19),
    ("Neha", 95, 21),
    ("Raj", 90, 20)
]

n = len(data)

# bubble sort
for i in range(n):
    for j in range(0, n - i - 1):
        
        # compare marks (descending)
        if data[j][1] < data[j + 1][1]:
            data[j], data[j + 1] = data[j + 1], data[j]
        
        # if marks equal → compare age (ascending)
        elif data[j][1] == data[j + 1][1]:
            if data[j][2] > data[j + 1][2]:
                data[j], data[j + 1] = data[j + 1], data[j]

print("Sorted Data:")
for item in data:
    print(item)


# Expected Output:

# Sorted Data:
# ('Neha', 95, 21)
# ('Raj', 90, 20)
# ('Riya', 90, 22)
# ('Karan', 85, 19)
# ('Aman', 85, 20)