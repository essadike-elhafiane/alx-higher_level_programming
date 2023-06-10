#!/usr/bin/python3
for i in range(0, 99):
    if i < 10:
        print("0{:d}, ".format(i), end='')
    else:
        print(f"{i}, ", end='')
print(i + 1)
