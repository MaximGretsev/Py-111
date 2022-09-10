from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    # TODO: Пересмотреть алгоритм
    right_border = len(arr) - 1
    left_border = 0
    while right_border >= left_border:
        mid_index = left_border + (right_border - left_border) // 2
        mid_value = arr[mid_index]
        if mid_value == elem:
            return mid_index
        elif elem < mid_value:
            right_border = mid_index - 1
        elif elem > mid_value:
            left_border = mid_index + 1
    return None
