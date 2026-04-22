# 3. Word Frequency Counter
# Given a file article.txt,
# Count frequency of each word (ignore case and punctuation).

def word_frequency():
    word_count = {}

    try:
        with open("Classwork/Improved File Handling/article.txt", "r") as file:
            for line in file:
                line = line.lower()

                # better punctuation handling
                for ch in ",.!?;:'\"()-":
                    line = line.replace(ch, "")

                words = line.split()

                for word in words:
                    word_count[word] = word_count.get(word, 0) + 1

        # sorted output
        for word in sorted(word_count):
            print(word, ":", word_count[word])

    except FileNotFoundError:
        print("Error: File not found")


word_frequency()