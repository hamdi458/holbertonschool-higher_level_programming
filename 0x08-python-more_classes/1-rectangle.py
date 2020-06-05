#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """Defines a Rectangle"""

    @property
    def width(self):
        """returns: int : rectongl width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setters"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns : int : rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setters"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """rectongle constructor"""
        self.height = height
        self.width = width
