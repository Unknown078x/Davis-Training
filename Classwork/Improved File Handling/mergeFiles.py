# 6. File Merge with Line Numbers
# You have two files: file1.txt and file2.txt.
# Merge them into a new file with line numbers.

def merge_files():
    try:
        with open("/Classwork/Improved File Handling/file1.txt", "r") as f1, \
             open("/Classwork/Improved File Handling/file2.txt", "r") as f2, \
             open("/Classwork/Improved File Handling/output.txt", "w") as out:

            line_number = 1

            for line in f1:
                out.write(f"{line_number}. {line.strip()}\n")
                line_number += 1

            for line in f2:
                out.write(f"{line_number}. {line.strip()}\n")
                line_number += 1

        print("Files merged with line numbers.")

    except FileNotFoundError:
        print("Error: One of the files not found")

    except IOError:
        print("Error: File handling issue")


merge_files()