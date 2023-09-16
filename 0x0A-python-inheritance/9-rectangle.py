#!/usr/bin/python3
"""
module: 9-rectangle
resources: a rectangle class that inherits from the
base class of BaseGeometry that contains the method
area implemented
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    This function validates the paameters given to
    an instance of Rectangle and initializes them
    as instance variables
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    """
    implementation of the area method
    """
    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
