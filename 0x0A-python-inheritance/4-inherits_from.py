#!/usr/bin/python3
"""
module: 4-inherits_from
resources: inherits_from(obj, a_class) function
"""


def inherits_from(obj, a_class):
    """
    checks if an object inherits from a class
    """
    if (type(obj) is not a_class and issubclass(type(obj), a_class)):
        return True
    return False
