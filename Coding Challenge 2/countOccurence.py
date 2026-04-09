# taking input string from the user
text = input("Enter string: ")
# taking the character whose frequency has to be calculated
char = input("Enter character to count: ")

count = 0

# loop to iterate through all the characters of the String
for ch in text:
    if ch == char:
        count += 1

print("Count:", count)