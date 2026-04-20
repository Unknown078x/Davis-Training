# program to get the array of elements that are divisible by 5 and greater than 50

import numpy as np
# creating array
data = np.array([45,36,54,67,49,20])
#checking which numbers are greater than 50
print("elements greater than 50: ")
print(data>50)
#creating array of elements that are divisible by 5
numbers2 = data/5
print("After dividing each element by 5")
print(numbers2)