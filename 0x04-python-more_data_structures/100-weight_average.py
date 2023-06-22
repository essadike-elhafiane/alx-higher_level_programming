#!/usr/bin/python3

def weight_average(my_list):
    if not my_list or not isinstance(my_list, list):
        return 0

    total_sum = 0
    total_weight = 0

    for score, weight in my_list:
        total_sum += score * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    return total_sum / total_weight
