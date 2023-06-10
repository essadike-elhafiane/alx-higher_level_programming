#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 97 <= ord(char) and 122 >= ord(char):
            print("{:s}".format(chr(ord(char) - 32)), end='')
        else:
            print(char, end='')
    print()
