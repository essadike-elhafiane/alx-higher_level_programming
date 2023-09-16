#!/usr/bin/python3
"""
module: 6-base_geometry
resources: class called BaseGeometry
containing a method called arae
"""


class BaseGeometry():
    """
    This class contains a method called area that raises an exception
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
