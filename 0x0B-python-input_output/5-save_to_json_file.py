#!/usr/bin/python3

"""
module: 5-save_to_json_file
resources: save_to_json_file() function, json module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Serialize python objects to JSON representation objects(strings)
    and and add it to a specified file
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
