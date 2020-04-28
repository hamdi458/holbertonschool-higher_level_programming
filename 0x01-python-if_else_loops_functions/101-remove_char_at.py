#!/usr/bin/python3
def remove_char_at(str, n):
    ch = ''
    for i in range(0, len(str)):
        if i != n:
            ch += str[i]
    return ch
