#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if length > 0:
        f_c = sentence[0]
    else:
        f_c = None
    return length, f_c
