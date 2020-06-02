#!/usr/bin/python3
""" class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle"""

    def __init__(self, width, height):
        """initialization"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """print() should print, and str() should return, the following
        rectangle description: [Rectangle] <width>/<height>."""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
