#!/usr/bin/python3
""" returns the number of lines of a text file:"""


def number_of_lines(filename=""):
    """ returns the number of lines of a text file:"""
    with open(filename, 'r', encoding='utf8') as file:
        sum = 0
        for i in file:
            sum += 1
        return sum
