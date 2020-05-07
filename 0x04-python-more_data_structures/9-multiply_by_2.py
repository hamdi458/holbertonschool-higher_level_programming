#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    di = a_dictionary
    return dict(zip(di.keys(), map(lambda x: 2*x, di.values())))
