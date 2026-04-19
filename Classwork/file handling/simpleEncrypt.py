# Question:11. File Encryption (Basic) Encrypt file content using a simple Caesar Cipher and save to new file.


# Algorithm:
# Step-1: taking shift value from user
# Step-2: opening the file in read mode
# Step-3: reading content of the file and save it in a variable
# Step-4: loop to iterate through the content of the file
# Step-5: checking if the word is alpha and is lower
# Step-6: now using the caesar cipher engine for encryption
# Step-7: opening new file in write mode and writing the encrypted values into it


# LOGIC:

shift = int(input("Enter shift value: "))

with open("input.txt", "r") as file:
    content = file.read()

encrypted = ""

for ch in content:
    if ch.isalpha():   # only letters
        if ch.islower():
            encrypted += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            encrypted += chr((ord(ch) - 65 + shift) % 26 + 65)
    else:
        encrypted += ch   # keep spaces, numbers same

with open("encrypted.txt", "w") as new_file:
    new_file.write(encrypted)

print("File encrypted successfully.")