# List utility module

def find_max(lst):
    """Find max"""
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val


def find_min(lst):
    """Find min"""
    min_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
    return min_val


def remove_duplicates(lst):
    """Remove duplicates"""
    return list(set(lst))


def second_largest(lst):
    """Second largest"""
    unique = list(set(lst))
    unique.sort()
    return unique[-2]


def sum_list(lst):
    """Sum of list"""
    return sum(lst)


def even_numbers(lst):
    """Return even numbers"""
    return [x for x in lst if x % 2 == 0]


def sort_list(lst):
    """Sort list"""
    return sorted(lst)