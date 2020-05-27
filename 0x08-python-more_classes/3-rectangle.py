#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """height.getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ rectangle area """
        return self.__height * self.__width

    def perimeter(self):
        """ rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """ print string with # """
        ch = ""
        if self.height == 0 or self.width == 0:
            return ch
        for i in range(self.height):
            for j in range(self.width):
                ch += '#'
            if i != self.height - 1:
                ch += '\n'
        return ch
