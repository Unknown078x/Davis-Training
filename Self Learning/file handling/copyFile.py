# Copy file without loading full file into memory

src = "data.txt"
dest = "copy.txt"

with open(src, "r") as f1, open(dest, "w") as f2:
    for line in f1:     # read line by line
        f2.write(line)

print("File copied")