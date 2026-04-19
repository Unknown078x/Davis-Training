# Word frequency

freq = {}

with open("data.txt", "r") as f:
    for word in f.read().split():
        freq[word] = freq.get(word, 0) + 1

print(freq)