# Problem: Email Extractor & Validator
# From a text file:
# • Extract emails
# • Validate format
# • Store unique emails

# Logic:
# 1. Open file and read line by line.
# 2. Split each line into words.
# 3. For each word:
#    - Check if it contains '@' and '.'
#    - Ensure only one '@'
#    - Ensure '.' comes after '@'
# 4. Clean common trailing symbols (, . ;)
# 5. Store valid emails in a set (for uniqueness).
# 6. Print all unique valid emails.

# Code:

file_path = "Lab Work/21-04-2026 Questions/emails.txt"

emails = set()

with open(file_path, "r") as file:
    for line in file:
        words = line.strip().split()
        
        for word in words:
            # remove common trailing punctuation
            word = word.strip(",.;")
            
            # basic validation
            if "@" in word and "." in word:
                if word.count("@") == 1:
                    at_index = word.index("@")
                    dot_index = word.rfind(".")
                    
                    if at_index < dot_index:
                        emails.add(word)

print("Valid Unique Emails:")
for email in emails:
    print(email)


# Expected Output (based on sample file below):

# Valid Unique Emails:
# test@gmail.com
# user123@yahoo.com
# hello.world@domain.in