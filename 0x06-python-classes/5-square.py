#!/usr/bin/python3
"""class Square."""


class Square:
    """class square."""

    def __init__(self, size):
        """Initialize square"""
        self.size = size

    @property
    def size(self):
        """Get/set the size of a square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the area of square."""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with #"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
