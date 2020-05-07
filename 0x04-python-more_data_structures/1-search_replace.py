#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        lt = my_list.copy()
        for i in range(len(lt)):
            if lt[i] == search:
                lt[i] = replace
    return(lt)
