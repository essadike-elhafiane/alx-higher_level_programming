#!/usr/bin/python3

class Student():
    def __init__(self, name="", age=None):
        self.name = name
        self.age = age

    def student_details(self):
        print(self.name)
        print(self.age)

