"""
Taylor series
"""
from typing import Union
import math
from itertools import count

# sin(x) -> ((-1) ** (n-1) * x ** (2n - 1)) / (2n - 1)!
EPSILON = 0.0001


def get_item_n(x, n):
    return x ** n / math.factorial(n)


def get_sin(x, n):
    return ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial((2 * n) + 1)


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    sum_ = 1
    for n in count(1, 1):
        current_item = get_item_n(x, n)
        sum_ += current_item
        if current_item <= EPSILON:
            break
    return sum_


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    sum_ = 0
    for n in count(0, 1):
        current_item = get_sin(x, n)
        print(current_item)
        sum_ += current_item

        if abs(current_item) <= EPSILON:
            break
    return sum_
