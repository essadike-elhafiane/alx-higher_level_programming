#!/usr/bin/python3
"""
module: 11-student
resources: a class called Student
"""


class Student():
    """
    classname: Student
    instance variables: first_name, last_name, age
    instance methods: to_json(self, attr=None), __init__,
    reload_from_json(self, json)
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        required_attr = dict(self.__dict__)
        if type(attr) is list:
            for item in self.__dict__:
                if item not in attr:
                    del(required_attr[item])
        return required_attr

    def reload_from_json(self, json):
        for key in json:
            self.__dict__[key] = json[key]
