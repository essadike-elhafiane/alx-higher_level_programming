#!/usr/bin/python3
stringg = ""

def uppercase(str):
    global stringg
    for char in str:
        if 97 <= ord(char) and 122 >= ord(char):
            stringg += chr(ord(char) - 32)
        else:
            stringg += char
    print("{:s}".format(stringg))
