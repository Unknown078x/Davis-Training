# given two arrays and we'll subtract them using numpy module

import numpy as np

# creating first array
arr1=np.array([10,40,120])
# creating second array
arr2=np.array([5,10,20])

# printing first array
print("First array:\n",arr1)
# printing Second array
print("Second array:\n",arr2)

# subtracting both arrays using subtract method of numpy
arr3=np.subtract(arr1,arr2)

# printing difference of arrays
print("Difference of arrays:\n",arr3)

