#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and type(my_list) == list:
        s = 0
        w = 0
        for s, w in my_list:
            s += s * w
            w += w
        return s/w
    return 0
