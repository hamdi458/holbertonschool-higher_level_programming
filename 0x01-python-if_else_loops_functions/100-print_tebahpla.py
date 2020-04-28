#!/usr/bin/python3
for i in range(122, 96, - 1):
    x = i
    if x % 2 != 0:
        x = x - 32
    print("{}".format(chr(x)), end="")
