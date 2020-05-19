#!/usr/bin/python3
"""class Square"""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize square"""
        self.size = size

    @property
    def size(self):
        """get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the current square"""
        return self.__size * self.__size
