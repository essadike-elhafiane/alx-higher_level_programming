#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    if (idx > len(my_list)):
        return None
    print("{:d}".format(my_list[idx]))
