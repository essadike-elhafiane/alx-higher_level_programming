#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    newlist = my_list;
    if idx < 0:
        return None
    if (idx >= len(my_list)):
        return None
    newlist[idx] = element
    return newlist
