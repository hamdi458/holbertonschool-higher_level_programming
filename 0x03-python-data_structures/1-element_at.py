#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if i == idx - 1:
            return(my_list[i])
    return(None)
