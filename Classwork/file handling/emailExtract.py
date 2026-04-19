# 5. Email Extractor From a file data.txt, Extract all valid email addresses and save them into emails.txt.

# Algorithm:
# Step-1: open the data file in read mode and convert the content into a list with seperation of spaces
# Step-2: opening email file in write mode 
# Step-3: reading the words from the list we created previously
# Step-4: checking emails
# Step-5: removing the common punctuations around the word
# Step-6: checking the valid format of the word
# Step-7: writing the email into email file



# LOGIC:

with open("Classwork/data.txt", "r") as file:
    words = file.read().split()

with open("Classwork/emails.txt", "w") as new_file:
    for word in words:
        # basic email check
        if "@" in word and "." in word:
            
            # remove common punctuation around word
            word = word.strip(",.!?()[]{}")
            
            parts = word.split("@")
            
            # check valid format (one @ and something before/after)
            if len(parts) == 2 and parts[0] != "" and "." in parts[1]:
                new_file.write(word + "\n")

print("Emails extracted.")