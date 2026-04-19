# Analyze file content

with open("data.txt", "r") as f:
    content = f.read()

lines = content.split("\n")
words = content.split()

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(content))