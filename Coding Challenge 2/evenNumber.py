# function to get even numbers only
def get_even(nums):
    result = []

    for n in nums:
        if n % 2 == 0:
            result.append(n)

    return result

print(get_even([1,2,3,4]))