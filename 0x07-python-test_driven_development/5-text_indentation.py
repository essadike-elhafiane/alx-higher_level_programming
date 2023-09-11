#!/usr/bin/python3
"""
Module: 5-text_indentation
Content: program that edits text by adding 2 newlines
after (.), (?) and (:).
"""


def text_indentation(text):
    """
    text_indentation function adds newline characters after the
    punctutions (.), (:) and (?).
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == "." or text[i] == ":" or text[i] == "?":
            print(text[i])
            print()
        else:
            if (i > 0 and text[i] == " " and (text[i - 1] == "." or
                                              text[i - 1] == ":" or
                                              text[i - 1] == "?" or
                                              text[i - 1] == " ")):
                continue
            print(text[i], end="")
