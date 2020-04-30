#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    s = 0
    for i in range(1, len(argv)):
        s = s + int(argv[i])
    print('{}'.format(s))
