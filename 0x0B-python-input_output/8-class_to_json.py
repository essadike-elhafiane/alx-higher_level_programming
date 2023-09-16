#!/usr/bin/python3
"""
module: 8-class_to_json
resources: class_to_json(obj) function
"""


def class_to_json(obj):
    """
    Takes a python object and extracts a JSON
    from it
    """
    return obj.__dict__
