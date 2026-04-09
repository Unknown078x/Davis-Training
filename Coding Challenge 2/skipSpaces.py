# taking input string from user
text = input("Enter string: ")

result = ""

# loop to iterate through all the characters of the String
for ch in text:
    # skip spaces
    if ch != " ":
        result += ch

print(result)