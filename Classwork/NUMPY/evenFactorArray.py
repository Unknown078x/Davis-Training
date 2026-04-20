# create a numpy array from the even factors of a given number

import numpy as np

num=int(input("Enter a number:"))

if num>0:
    nums = np.arange(1, num + 1)

    # num%nums==0 tells which numbers from the array divides the given number and nums%2==0 tells which numbers are even then & operator works as AND which will return true if both conditions are true
    div = (num % nums == 0) & (nums % 2 == 0)

    print(nums[div])
elif num<0:
    print("Give positive number")
else:
    print("Zero number given")