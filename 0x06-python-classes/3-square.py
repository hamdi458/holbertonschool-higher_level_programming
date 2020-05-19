#!/usr/bin/python3
"""a class Square"""


class Square:
    """class Square"""
    def __init__(self, size=0):
        """initialize a square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current area"""
        return self.__size * self.__size
