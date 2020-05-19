#!/usr/bin/python3
"""class Square"""


class Square:
    """ class square"""
    def __init__(self, size=0):
    """Initialize a square."""
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        """Get the current size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setters"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square"""
        return self.__size * self.__size
