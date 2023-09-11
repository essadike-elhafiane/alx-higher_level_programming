#!/usr/bin/python3

"""
Module: 4-print_square
Content: Contains a program that prints a square
using #
"""


def print_square(size):
    """
    The function print_square takes an argument size
    and prints a square of side == size

    It checks is if size is of type integer or if
    size is less than 0. If that is the case
    exceptions are raised
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    for i in range(size):
        print('#' * size)
