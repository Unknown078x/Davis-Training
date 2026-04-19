# Replace word

old = input("Word to replace: ")
new = input("New word: ")

with open("data.txt", "r") as f:
    content = f.read()

content = content.replace(old, new)

with open("data.txt", "w") as f:
    f.write(content)

print("Replacement done")