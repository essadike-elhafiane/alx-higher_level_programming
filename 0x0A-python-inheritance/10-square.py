#!/usr/bin/python3
"""
module: 10-square
resources: the Square class that inherits from
Rectangle
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Initialize the Ssquare instances by defining an
    __init__ method that calls the __init__ method
    of the parent and passing size to both parameters
    of height and width
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
