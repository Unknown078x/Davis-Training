# Log errors

try:
    x = int(input("Enter number: "))
    print(10 / x)

except Exception as e:
    with open("error.log", "a") as f:
        f.write(str(e) + "\n")

    print("Error logged")