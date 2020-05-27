#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """class rectangle
    Attributes:
        height (int): Height of the rectangle
        width (int): Width of the rectangle
    """

    @property
    def width(self):
        """rectangle width
        Returns:
        int: Recangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets rectangle width value
        Args:
        value (int): Rectangle's width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """rectangle height
        Returns:
        int: Recangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setters
        Args:
        value (int): Rectangle's height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """constructor
        Args:
            width (int): default value 0
            height (int): default value 0"""
        self.height = height
        self.width = width

    def area(self):
        """rectangle area
        Return: int"""
        return self.__width*self.__height

    def perimeter(self):
        """rectangle perimeter
        Returns: int"""
        if self.width == 0 or self.__height == 0:
            return 0
        return (self.__width*2) + (self.__height*2)
