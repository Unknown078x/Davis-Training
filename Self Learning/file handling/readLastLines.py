# Read last N lines

n = int(input("Enter number of lines: "))

with open("data.txt", "r") as f:
    lines = f.readlines()

for line in lines[-n:]:
    print(line.strip())