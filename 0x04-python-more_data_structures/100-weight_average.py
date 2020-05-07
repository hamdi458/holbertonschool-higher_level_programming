#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None and type(my_list) == list:
        return 0
    s, w = 0, 0
    for score, weight in my_list:
        s += score * weight
        w += weight
    return s/w
