#!/usr/bin/python3

"""
module: 3-to_json_string
resources: to_json_string() function
"""
import json


def to_json_string(my_obj):
    """
    This function serializes python objects to
    JSON representation of an object(string)
    """
    return json.dumps(my_obj)
