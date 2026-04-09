# taking input sentence from the user
text = input("Enter sentence: ")

# adding all the words of the sentence to the list
words = text.split()

# let the first word be the longest 
longest = words[0]

# loop to iterate through all the words of the list
for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)