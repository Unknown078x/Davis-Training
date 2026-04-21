# problem statement
# 7. File Word Frequency Analyzer
# Read a large file:
# • Count word frequency
# • Ignore stop words
# • Show top 10 words 



# logic:
# take all the stop words
# open the file
# remove punctuations and special symbols
# remove stop words 
# count frequency
# sort the words with their frequencies in descending order
# show top 10 words


# Basic stop words
stopWords = {
    'the', 'is', 'in', 'and', 'to', 'of', 'a', 'on', 'for', 'with',
    'as', 'by', 'at', 'an', 'be', 'this', 'that', 'it', 'from'
}

with open("Classwork/21-04-2026 Questions/sampleFile.txt", "r") as file:
    text = file.read().lower()

# Remove punctuation manually
cleanedText = ""
for char in text:
    # removing punctuation by keeping the letters, numbers and spaces only
    if char.isalnum() or char.isspace(): 
        cleanedText += char
    else:
        cleanedText += " "  # replace punctuation with space

# Split into words
words = cleanedText.split()

# Remove stop words
finalWords = []
for word in words:
    if word not in stopWords:
        finalWords.append(word)

# Count frequency manually
wordCount = {}

for word in finalWords:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

# sort dictionary by value (frequency)
sortedWords = sorted(wordCount, key=wordCount.get, reverse=True)


print("Top 10 words:")
for word in sortedWords[:10]:
    print(word, ":", wordCount[word])





# OUTPUT:
# Top 10 words:
# you : 15
# writing : 10
# s : 8
# article : 7
# me : 5
# what : 5
# write : 5
# i : 5
# not : 4
# easy : 4
