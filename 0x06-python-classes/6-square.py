#!/usr/bin/python3
"""class Square."""


class Square:
    """class square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get  position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if len(value) == 2 and type(value) == tuple and\
        type(value[0]) == int and value[0] >= 0 and\
        type(value[1]) == int and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Return the area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with #"""
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.position[0]):
                print(end=' ')
            for k in range(self.size):
                print("#", end='')
            print()
