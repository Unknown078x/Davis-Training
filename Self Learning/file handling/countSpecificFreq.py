# Count occurrences of a word

word = input("Enter word: ")

count = 0

with open("data.txt") as f:
    for line in f:
        count += line.split().count(word)

print("Occurrences:", count)