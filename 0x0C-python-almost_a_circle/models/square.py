#!/usr/bin/python3
"""
module: square
resources: a class named Square that inherits
from Rectangle
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    This is a class Square that inherits from
    rectangle it contains a method called size
    that sets the width and height to be the
    same value
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        This method initializes instance variables of
        a square object using the super class
        """
        super().__init__(x=x, y=y, width=size, height=size, id=id)

    @property
    def size(self):
        """
        This method return the length of the
        side of a square
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        This method sets the length of the side
        of a square
        """
        self.width = size
        self.height = size

    def __str__(self):
        """
        This method is a magical method that returns
        the form in which the object will be represented
        when called with print() or str()
        """
        return "[Square] ({}) {}/{} - {}".format(
                                                 self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
        """
        This method modifies the field of a square
        object previously created
        """
        arg_count = len(args)
        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            if key == 'size':
                self.size = value
            if key == 'x':
                self.x = value
            if key == 'y':
                self.y = value

        if arg_count > 0:
            self.id = args[0]
        if arg_count > 1:
            self.size = args[1]
        if arg_count > 2:
            self.x = args[2]
        if arg_count > 3:
            self.y = args[3]

    def to_dictionary(self):
        """
        to_dictionary returns a dictionary of instance
        attributes such as id, width, height, x and y
        """
        final_dict = {}
        prefix = '_Rectangle__'
        for key, value in self.__dict__.items():
            if 'height' in key or 'width' in key:
                continue
            if prefix in key:
                key = key.replace(prefix, '')
            final_dict[key] = value
        final_dict['size'] = self.size
        return final_dict
