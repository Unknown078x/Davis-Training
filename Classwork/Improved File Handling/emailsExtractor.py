# 5. Email Extractor
# From a file data.txt,
# Extract all valid email addresses and save them into emails.txt.

def extract_emails():
    try:
        with open("Classwork/Improved File Handling/emails.txt", "r") as file, \
             open("Classwork/Improved File Handling/extractedEmails.txt", "w") as new_file:

            for line in file:
                words = line.split()

                for word in words:
                    word = word.strip(",.!?()[]{}").lower()

                    parts = word.split("@")

                    if len(parts) == 2:
                        local, domain = parts

                        if local and "." in domain:
                            new_file.write(word + "\n")

        print("Emails extracted.")

    except FileNotFoundError:
        print("Error: File not found")

    except IOError:
        print("Error: File handling issue")


extract_emails()