#!/usr/bin/python3
"""
module: 9-student
resources: a class called Student
"""


class Student():
    """
    classname: Student
    instance variables: first_name, last_name, age
    instance methods: to_json(self), __init__
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
