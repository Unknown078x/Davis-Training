# taking input from user 
text = input("Enter string: ")

count = 0

# loop to iterate through all the characters of the String
for ch in text:
    # check each character
    if ch.lower() in "aeiou":
        count += 1

print("Vowels:", count)