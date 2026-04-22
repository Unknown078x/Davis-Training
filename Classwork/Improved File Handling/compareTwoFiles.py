# Question:10. Compare Two Files Find lines that are present in file1 but not in file2.


def compare_files():
    try:
        with open("Classwork/Improved File Handling/file2.txt", "r") as f2:
            set2 = {line.strip().lower() for line in f2}

        with open("Classwork/Improved File Handling/file1.txt", "r") as f1:
            for line in f1:
                clean_line = line.strip().lower()

                if clean_line not in set2:
                    print(line, end="")

    except FileNotFoundError:
        print("Error: File not found")

    except IOError:
        print("Error: File handling issue")


compare_files()