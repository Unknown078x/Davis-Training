# Remove empty lines

with open("data.txt", "r") as f:
    lines = f.readlines()

with open("clean.txt", "w") as f:
    for line in lines:
        if line.strip():   # ignore empty lines
            f.write(line)

print("Cleaned file created")