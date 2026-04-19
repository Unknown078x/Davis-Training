# Merge two files into one

with open("file1.txt") as f1, open("file2.txt") as f2:
    content = f1.read() + "\n" + f2.read()

with open("merged.txt", "w") as f:
    f.write(content)

print("Files merged")