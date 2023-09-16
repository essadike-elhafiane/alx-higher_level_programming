#!/usr/bin/python3
"""
module: 3-is_kind_of_class
resources: is_kind_of_class(obj, a_class) function
"""


def is_kind_of_class(obj, a_class):
    """
    checks if an object is an instance of a class or if the object is an
    instance of a class that inherited from the specified class
    """
    if isinstance(obj, a_class):
        return True
    return False
