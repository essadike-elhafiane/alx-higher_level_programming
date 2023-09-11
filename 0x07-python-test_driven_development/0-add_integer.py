#!/usr/bin/python3
"""
Module Name: 0-add_integer
Contains a function that adds 2 numbers
"""


def add_integer(a, b=98):
    """
    This function takes 2 values as input

    Returns the sum
    """
    if (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
