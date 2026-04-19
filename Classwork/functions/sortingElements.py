numbers = [20,19,222,56,33,2,0,21,67,53]

# loop to iterate through the list
for i in range(len(numbers)):
    # assuming the first element to be the biggest element and saving its index
    maxElement = i
    
    # second loop to iterate through the list to compare the other elements with the first element
    for j in range(i+1, len(numbers)):
        # checking if the next element is greater than the assumed max element, if true replace the index
        if numbers[j] > numbers[maxElement]:
            maxElement = j
    
    # after the iterations of second loop, replacing the highest element to the first position and so on
    numbers[i], numbers[maxElement] = numbers[maxElement], numbers[i]

# printing the elements in descending order
print("Sorted list in descending order:", numbers)