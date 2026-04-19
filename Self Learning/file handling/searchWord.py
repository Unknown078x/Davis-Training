# Search for a word

word = input("Enter word: ")

with open("data.txt", "r") as f:
    found = False
    for line in f:
        if word in line:
            found = True
            print("Found in line:", line.strip())

if not found:
    print("Word not found")