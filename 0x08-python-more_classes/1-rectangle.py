#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """Defines a Rectangle"""

    @property
    """Returns: int: Recangle width"""
    def width(self):
        return self.__width
    @width.setter
    """setters"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
       """Returns:
        int: Recangle's height"""
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """rectongle constructor"""
        self.height = height
        self.width = width
