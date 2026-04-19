# Question:Given a file article.txt, Count frequency of each word (ignore case and punctuation).

# Algorithm:
# Step-1: open the article file in read mode
# Step-2: read the article file line by line
# Step-3: convert the line into lowercase to ignore case senstivity
# Step-4: replace all the punctuation with spaces, as we just want to count words
# Step-5: convert the line into a list using split by seperation of spaces
# Step-6: now count the frequencies of words and put it in the dictionary
# Step-6: printing the words with their count

# LOGIC


# Dictionary to store word counts
word_count = {}

with open("Classwork/article.txt", "r") as file:
    for line in file:
        # convert to lowercase (ignore case)
        line = line.lower()
        
        # replace punctuation with spaces
        line = line.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
        
        # split into words
        words = line.split()

        # count frequency
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

# print result
for word, count in word_count.items():
    print(word, ":", count)