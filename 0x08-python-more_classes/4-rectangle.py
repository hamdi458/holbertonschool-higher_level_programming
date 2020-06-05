#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """class rectanngle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """rectangle width getter"""
        return self.__width

    @property
    def height(self):
        """ rectangle heigth getter"""
        return self.__height

    @width.setter
    def width(self, value):
        """rectangle width setter"""
        if type(value) == int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        """height rectangle setter"""
        if type(value) == int:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """rectangle preimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """ print rect with # """
        ch = ""
        if self.__width == 0 or self.__height == 0:
            return str
        ch += "\n".join("#" * self.__width
                        for j in range(self.__height))
        return ch

    def __repr__(self):
        """return a string"""
        return 'Rectangle({}, {})'.format(self.width, self.height)
