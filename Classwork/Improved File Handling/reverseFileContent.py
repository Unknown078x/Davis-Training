# 7. Reverse File Content
# Read a file and write its content in reverse order (line-wise) into another file.


def reverse_file():
    try:
        with open("Classwork/Improved File Handling/content.txt", "r") as file:
            lines = file.readlines()

        with open("Classwork/Improved File Handling/output.txt", "w") as new_file:
            for line in reversed(lines):
                new_file.write(line)

        print("File reversed successfully.")

    except FileNotFoundError:
        print("Error: File not found")

    except IOError:
        print("Error: File handling issue")


reverse_file()