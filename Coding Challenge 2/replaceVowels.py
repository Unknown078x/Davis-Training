# taking input string from the user
text = input("Enter string: ")

result = ""

# loop to iterate through all the characters of the String
for ch in text:
    if ch.lower() in "aeiou":
        result += "*"
    else:
        result += ch

print(result)