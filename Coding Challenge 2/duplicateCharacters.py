# taking input string from user
text = input("Enter string: ")

seen = []
duplicates = []

# loop to iterate through all the characters of the String
for ch in text:
    if ch in seen and ch not in duplicates:
        duplicates.append(ch)
    else:
        seen.append(ch)

print("Duplicates:", " ".join(duplicates))