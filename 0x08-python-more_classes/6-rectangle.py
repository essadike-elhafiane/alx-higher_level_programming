#!/usr/bin/python3

# 6-rectangle module
"""
This module contains a class Rectangle

>>> Rectangle = __import__('6-rectangle').Rectangle

>>> my_rectangle = Rectangle(2, 4)
>>> print(type(my_rectangle))
<class '6-rectangle.Rectangle'>

>>> dict_result = my_rectangle.__dict__
>>> print(dict(sorted(dict_result.items())))
{'_Rectangle__height': 6, '_Rectangle__width': 2}

"""


class Rectangle:
    """This is an class Rectangle with instance attribute heigth and width"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        initializes height and width of the rectangle
        upon creation of an instance using property
        getters and setters

        >>> my_rectangle = Rectangle(2, '4')
        Traceback (most recent call last):
            ...
        TypeError: height must be an integer


        >>> my_rectangle = Rectangle(0, 0)
        >>> my_rectangle.width = 10
        >>> my_rectangle.height = -3
        Traceback (most recent call last):
            ...
        ValueError: height must be >= 0
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Property getter for the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """
        Property setter for the width
        checks if the type for the width is an integer or < 0
        if above conditions aren't met errors are raised
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Property getter for the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """
        Property setter for the height
        checks if the type for the height is an integer or < 0
        if above conditions aren't met errors are raised
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """
        The method area() returns the area of the rectangle
        by taking the product of the width and height of the
        rectangle instance

        >>> my_rectangle = Rectangle(5, 8)
        >>> my_rectangle.area()
        40
        """
        return self.width * self.height

    def perimeter(self):
        """
        The method perimeter() return the perimeter of the
        rectangle by taking the sum of width and height of the
        rectangle, then multiplying the result by 2

        If the width or height of the rectangle is 0 the 0 is
        returned

        >>> my_rectangle = Rectangle(5, 8)
        >>> my_rectangle.perimeter()
        26
        >>> my_rectangle.height = 0
        >>> my_rectangle.perimeter()
        0
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        The method __str__() is used to return the representation (drawing)
        of the rectangle instance using #

        If the width or the height is 0 an empty string is returned
        """
        if self.width == 0 or self.height == 0:
            return ""
        shape_rep_array = []
        for height in range(self.height):
            shape_rep_array.append("#" * self.width)
            shape_rep_array.append("\n")
        shape_rep_array.pop()
        return "".join(shape_rep_array)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
