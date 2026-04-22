# Question:11. File Encryption (Basic) Encrypt file content using a simple Caesar Cipher and save to new file.


def encrypt_file():
    try:
        shift = int(input("Enter shift value: "))
        result = []

        with open("input.txt", "r") as file:
            for line in file:
                for ch in line:
                    if ch.isalpha():
                        if ch.islower():
                            result.append(chr((ord(ch) - 97 + shift) % 26 + 97))
                        else:
                            result.append(chr((ord(ch) - 65 + shift) % 26 + 65))
                    else:
                        result.append(ch)

        with open("encrypted.txt", "w") as new_file:
            new_file.write("".join(result))

        print("File encrypted successfully.")

    except ValueError:
        print("Error: Shift must be an integer")

    except FileNotFoundError:
        print("Error: Input file not found")

    except IOError:
        print("Error: File handling issue")


encrypt_file()