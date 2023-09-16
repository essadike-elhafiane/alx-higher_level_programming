#!/usr/bin/python3
"""
module: 10-square
resources: the Square class that inherits from
Rectangle
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle, BaseGeometry):
    """
    Initiliaze the square using size parameter
    """
    def __init__(self, size):
        """
        This method intializes the values given as parameter
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        implementing area of a square
        """
        return (self.__size * self.__size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
