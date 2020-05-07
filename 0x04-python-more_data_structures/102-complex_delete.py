#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dic = a_dictionary.copy()
    for x, y in new_dic.items():
        if y == value:
            del a_dictionary[x]
    return a_dictionary
