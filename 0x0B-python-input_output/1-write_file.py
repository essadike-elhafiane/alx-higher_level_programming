#!/usr/bin/python3

"""
module: 1-write_file
resources: write_file() function
"""


def write_file(filename="", text=""):
    """
    The program in this function write some given text
    to a specified file
    """
    with open(filename, "w", encoding="utf-8") as file:
        num_of_text_written = file.write(text)
    return num_of_text_written
