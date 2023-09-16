#!/usr/bin/python3

"""
module: 4-from_json_string
resources: from_json_string()
"""
import json


def from_json_string(my_str):
    """
    Deserializes JSON object representaion(strings)
    to python objects
    """
    return json.loads(my_str)
