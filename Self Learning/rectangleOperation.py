# Function to calculate the area of a rectangle
def calculate_area(length, width):
    area = length * width
    return area

# Function to calculate the perimeter of a rectangle
def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Check if dimensions are non-negative
if length < 0 or width < 0:
    print("Length and width cannot be negative. Please enter positive values.")
else:
    # Calculate area using the function
    area = calculate_area(length, width)
    # Calculate perimeter using the function
    perimeter = calculate_perimeter(length, width)

    # Display the results
    print(f"The area of the rectangle is: {area}")
    print(f"The perimeter of the rectangle is: {perimeter}")