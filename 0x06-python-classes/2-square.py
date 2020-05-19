#!/usr/bin/python3
"""class square"""


class Square:
    """class of a square"""
    def __init__(self, size=0):
        """Initializes a attribute
        Args:
            size (int): size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
