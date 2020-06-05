#!/usr/bin/python3
"""reads n lines of a text file"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file (UTF8) and prints it to stdout"""
    number_of_lines = __import__('1-number_of_lines').number_of_lines
    with open(filename, encoding="UTF-8") as file:
        if nb_lines <= 0 or nb_lines >= number_of_lines(filename):
            print(file.read(), end='')
        else:
            sum_line = 1
            while sum_line <= nb_lines:
                print("{}".format(file.readline()), end="")
                sum_line += 1
