numbers = [12, 5, 8, 23, 1, 45, 9, 3, 17, 6]

# loop to iterate through the list
for i in range(len(numbers)):
    # assuming the first element to be the biggest element and saving its index
    max = i
    
    # second loop to iterate through the list to compare the other elements with the first element
    for j in range(i+1, len(numbers)):
        # checking if the next number is greater than the assumed max number, if true replace the index
        if numbers[j] > numbers[max]:
            max = j
    
    # after the iterations of second loop, replacing the highest number to the first position and so on
    numbers[i], numbers[max] = numbers[max], numbers[i]

# printing the elements in descending order
print("Sorted list in descending order:", numbers)