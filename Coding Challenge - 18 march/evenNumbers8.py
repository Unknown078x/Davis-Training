# recursive function
def print_even(n, i=2):
    if i > n:
        return
    print(i, end=" ")
    print_even(n, i + 2)

# taking input
n = int(input("Enter N: "))
print_even(n)