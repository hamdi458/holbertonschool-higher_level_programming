#!/usr/bin/python3
def no_c(my_string):
    ch = ""
    for x in my_string:
        if x is not 'c' and x is not 'C':
            ch += x
    return(ch)
