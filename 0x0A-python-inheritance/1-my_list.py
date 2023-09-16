#!/usr/bin/python3
"""
Module: 1-my_list
resources: MyList class
"""


class MyList(list):
    """
    MyList is a class that inherites the list object.
    """
    def print_sorted(self):
        print(sorted(self))
