# taking input string from the user
text = input("Enter string: ")

result = ""

# loop to iterate through all the characters of the String
for ch in text:
    # check if lowercase letter
    if 'a' <= ch <= 'z':
        # convert using ASCII difference
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)