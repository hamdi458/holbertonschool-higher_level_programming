#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = ord(i)
        if c >= 97 and c <= 122:
            c = ord(i) - 32
        print("{}".format(chr(c)), end="")
    print()
