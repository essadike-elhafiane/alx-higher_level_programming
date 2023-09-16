#!/usr/bin/python3
"""
module: 6-load_from_json_file
resources: load_from_json_file() function
"""
import json


def load_from_json_file(filename):
    """
    Deserialize strings from specified file
    """
    with open(filename) as file:
        py_obj = json.load(file)
    return py_obj
