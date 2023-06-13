#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    maxn = my_list[0]
    for n in my_list[1:]:
        if n > maxn:
            maxn = n
    return maxn
