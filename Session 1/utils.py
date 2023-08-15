def find_max(lst):
    """
    This function takes a list of numbers as input and returns the maximum number in the list.

    Args:
    lst (list): A list of numbers.

    Returns:
    int or float: The maximum number in the list.

    """

    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num



def bubble_sort(lst):
    """
    This function takes a list of numbers as input and sorts the list using the bubble sort algorithm.

    Args:
    lst (list): A list of numbers.

    Returns:
    list: The sorted list of numbers.

    """

    n = len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst



def find_sum(lst):
    """
    This function takes a list of numbers as input and returns the sum of all the numbers in the list.

    Args:
    lst (list): A list of numbers.

    Returns:
    int or float: The sum of all the numbers in the list.

    """

    total = 0
    for num in lst:
        total += num
    return total


def find_mean(lst):
    """
    This function takes a list of numbers as input and returns the mean (average) of all the numbers in the list.

    Args:
    lst (list): A list of numbers.

    Returns:
    int or float: The mean (average) of all the numbers in the list.

    """

    n = len(lst)
    total = find_sum(lst)
    mean = total / n
    return mean
