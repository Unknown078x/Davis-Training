# taking input string from user
text = input("Enter string: ")

# reverse string using slicing
rev = text[::-1]

if text == rev:
    print("Yes")
else:
    print("No")