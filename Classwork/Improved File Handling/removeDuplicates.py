# 4. Remove Duplicate Lines
# A file contains repeated lines due to logging errors.
# Create a new file with only unique lines (preserve order).

def remove_duplicates():
    seen = set()

    try:
        with open("Classwork/Improved File Handling/article.txt", "r") as file, \
             open("Classwork/Improved File Handling/output.txt", "w") as new_file:

            for line in file:
                clean_line = line.strip()  # remove extra spaces/newline

                if clean_line not in seen:
                    new_file.write(clean_line + "\n")
                    seen.add(clean_line)

        print("Duplicate lines removed.")

    except FileNotFoundError:
        print("Error: File not found")

    except IOError:
        print("Error: File handling issue")


remove_duplicates()