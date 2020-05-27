#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """class rectangle"""

    @property
    def width(self):
        """ width reeturn int: Recangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter
        Args: width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return int
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setters
        Args:
        value (int): Rectangle's height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """constructor
        Args:
            width (int):width
            height (int):height"""
        self.height = height
        self.width = width

    def area(self):
        """
        rectangle area
        """
        return self.__width*self.__height

    def perimeter(self):
        """rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width*2) + (self.__height*2)

    def __str__(self):
        """
        print rectangles"""
        ch = ""
        if self.__width == 0 or self.__height == 0:
            return str
        ch += "\n".join("#" * self.__width
                         for j in range(self.__height))
        return ch
