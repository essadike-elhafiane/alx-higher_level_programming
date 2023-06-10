#!/usr/bin/python3

def uppercase(str):
    stringg = ""
    for char in str:
        if 97 <= ord(char) and 122 >= ord(char):
            stringg += chr(ord(char) - 32)
        else:
            stringg += char
    print("{:s}".format(stringg))
