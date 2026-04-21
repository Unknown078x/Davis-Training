# Problem: Palindrome Sentence Analyzer
# Given sentences:
# • Detect palindrome words
# • Count frequency
# Ignore spaces and case

# Logic:
# 1. Read input sentence.
# 2. Convert sentence to lowercase (ignore case).
# 3. Split sentence into words.
# 4. Clean each word (remove punctuation).
# 5. Check if word == reverse(word) and length > 1.
# 6. Use dictionary to count frequency of palindrome words.
# 7. Print results.

# Code:

sentence = input("Enter sentence: ")

# convert to lowercase
sentence = sentence.lower()

# split into words
words = sentence.split()

palindrome_count = {}

for word in words:
    # remove common punctuation
    word = word.strip(",.!?;:")
    
    # check palindrome
    if len(word) > 1 and word == word[::-1]:
        if word in palindrome_count:
            palindrome_count[word] += 1
        else:
            palindrome_count[word] = 1

print("Palindrome Words Frequency:")
for word, count in palindrome_count.items():
    print(word, "->", count)


# Expected Output (example):

# Input:
# Enter sentence: Madam Arora teaches malayalam level civic civic test

# Output:
# Palindrome Words Frequency:
# madam -> 1
# arora -> 1
# malayalam -> 1
# level -> 1
# civic -> 2