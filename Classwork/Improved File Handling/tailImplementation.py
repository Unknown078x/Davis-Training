# Question:12. Tail Implementation (Like Linux tail) Display last N lines of a file efficiently.


def print_last_lines():
    try:
        n = int(input("Enter number of lines: "))

        if n <= 0:
            print("Please enter a positive number")
            return

        with open("input.txt", "r") as file:
            lines = file.readlines()

        for line in lines[-n:]:
            print(line, end="")

    except ValueError:
        print("Error: Please enter a valid integer")

    except FileNotFoundError:
        print("Error: File not found")

    except IOError:
        print("Error: File handling issue")


print_last_lines()