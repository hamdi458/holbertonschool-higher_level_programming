#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize consrtructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get width"""
        return self.__width

    @property
    def height(self):
        """get height"""
        return self.__height

    @property
    def x(self):
        """get x"""
        return self.__x

    @property
    def y(self):
        """get y"""
        return self.__y



    @width.setter
    def width(self, valeur):
        if type(valeur) is not int:
            raise TypeError("width must be an integer")
        if valeur <= 0:
            raise ValueError("width must be > 0")
        self.__width = valeur

    @height.setter
    def height(self, valeur):
        if type(valeur) is not int:
            raise TypeError("height must be an integer")
        if valeur <= 0:
            raise ValueError("height must be an integer")
        self.__height = valeur

    @x.setter
    def x(self, valeur):
        if type(valeur) != int:
            raise TypeError("x must be an integer")
        if valeur < 0:
            raise ValueError("x must be >= 0")
        self.__x = valeur

    @y.setter
    def y(self, valeur):
        if type(valeur) != int:
            raise TypeError("y must be an integer")
        if valeur < 0:
            raise ValueError("y must be >= 0")
        self.__y = valeur

    def area(self):
        """return area"""
        return self.width * self.height

    def display(self):
        print("\n".join("#" * self.width for i in range(self.height)))
