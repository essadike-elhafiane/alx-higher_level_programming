#!/usr/bin/python3

"""
module: base
resources: class Base, which is the base class of all class
in this project
"""
import json


class Base:
    """
    The goal of this class is to manage the id attribute in
    all the future classes of this project and to avoid code
    duplication (by extension, bug duplication)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This method initializes the the instance variables
        of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This method takes a python object and converts
        it to a json string
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This method takes a python object, converts it
        to a json string then saves it to a json file
        """
        new_list_objs = []
        if type(list_objs) is list:
            for item in list_objs:
                new_list_objs.append(item.to_dictionary())
        filename = "{}.json".format(cls.__name__)
        file_contents = Base.to_json_string(new_list_objs)
        with open(filename, 'w') as file:
            file.write(file_contents)

    @staticmethod
    def from_json_string(json_string):
        """
        This method returns a python object from a json
        string
        """
        if json_string is None or json_string == '':
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        This method creates a new object
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        This method retrieves a list of instances
        from a file with similar name as the class
        which called the method
        """
        list_of_instances = []
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename) as file:
                # str_list_of_dict - is a json string representation of
                # a list of str_list_of_dict - is a json string
                # representation of a list of dictionaries containing
                # instances variables(fields) with their values
                str_list_of_dict = file.read()
        except FileNotFoundError:
            return []
        else:
            list_output = cls.from_json_string(str_list_of_dict)
            for dictionary in list_output:
                list_of_instances.append(cls.create(**dictionary))
        return list_of_instances
