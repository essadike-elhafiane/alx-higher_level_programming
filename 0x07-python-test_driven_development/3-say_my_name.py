#!/usr/bin/python3
"""
Module: 3-say_my_name
Contents: function that prints the name of a person
"""


def say_my_name(first_name, last_name=""):
    """
    The function say_my_name checks if first_name
    and last_name are strings

    Then uses format to print the complete name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
