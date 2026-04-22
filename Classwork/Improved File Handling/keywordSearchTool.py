# Question:8. Keyword Search Tool Ask user for a keyword and return all lines from file containing that keyword.

def search_keyword():
    keyword = input("Enter keyword: ").lower()
    found = False

    try:
        with open("Classwork/Improved File Handling/content.txt", "r") as file:
            for line in file:
                if keyword in line.lower():
                    print(line, end="")
                    found = True

        if not found:
            print("No matching lines found.")

    except FileNotFoundError:
        print("Error: File not found")

    except IOError:
        print("Error: File handling issue")


search_keyword()