#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    s, w = 0, 0
    for score, weight in my_list:
        s += score * weight
        w += weight
    return s/w
