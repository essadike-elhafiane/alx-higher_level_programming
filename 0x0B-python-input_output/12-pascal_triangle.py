#!/usr/bin/python3
"""
module: 12-pascal_triangle
resources: pascal_triangle function - returns a representation
of the pascal triangle in the form of a 2 dimension list
"""


def pascal_triangle(n):
    """
    Algorithm
    =========
    1. create an a list called overall_list
    2. check if n <= 0, if so return empty list
    3. create an outer for loop with range(0, n) - "i"
    as the iterating variable
    4. check if the outer loop is past the 1st iteration,
    and create a list pre_list if that is the case
    5. create an empty list, calling it cur_list
    6. create an inner loop with range(0, i+1) - "j" as
    the inner iterating variable
    7. check if the inner loop is at the 1 iteration or
    last iteration and append 1 if that's the case
    8. else, append the sum of prev_list[j] and prev_list[j-1]
    9. append the cur_list to the overall_list
    10. return the overall list
    """
    overall_list = []
    if n <= 0:
        return []
    for i in range(0, n):
        if i > 0:
            prev_list = overall_list[i - 1]
        cur_list = []
        for j in range(0, i+1):
            if j == 0 or j == i:
                cur_list.append(1)
            else:
                cur_list.append(prev_list[j] + prev_list[j - 1])
        overall_list.append(cur_list)
    return overall_list
