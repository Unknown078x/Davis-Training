# Question:9. Find Longest Line Identify the longest line in a file and print its length and content.


def longest_line():
    max_line = None
    max_length = 0

    try:
        with open("/Classwork/Improved File Handling/content.txt", "r") as file:
            for line in file:
                clean_line = line.strip()

                if len(clean_line) > max_length:
                    max_length = len(clean_line)
                    max_line = clean_line

        if max_line is None:
            print("File is empty")
        else:
            print("Longest line length:", max_length)
            print("Longest line:", max_line)

    except FileNotFoundError:
        print("Error: File not found")

    except IOError:
        print("Error: File handling issue")


longest_line()