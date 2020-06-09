#!/usr/bin/python3
"""heritage rectangle from base"""
from models.base import Base


class Rectangle(Base):
    """class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize consrtructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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
        """setters"""
        if type(valeur) is not int:
            raise TypeError("width must be an integer")
        if valeur <= 0:
            raise ValueError("width must be > 0")
        self.__width = valeur

    @height.setter
    def height(self, valeur):
        """setters"""
        if type(valeur) is not int:
            raise TypeError("height must be an integer")
        if valeur <= 0:
            raise ValueError("height must be an integer")
        self.__height = valeur

    @x.setter
    def x(self, valeur):
        """setters x"""
        if type(valeur) is not int:
            raise TypeError("x must be an integer")
        if valeur < 0:
            raise ValueError("x must be >= 0")
        self.__x = valeur

    @y.setter
    def y(self, valeur):
        """setters y"""
        if type(valeur) is not int:
            raise TypeError("y must be an integer")
        if valeur < 0:
            raise ValueError("y must be >= 0")
        self.__y = valeur

    def area(self):
        """return area"""
        return self.width * self.height

    def display(self):
        """display"""
        print("\n" * self.y + "\n".join(" " * self.x + "#" * self.width
                                        for i in range(self.height)))

    def __str__(self):
        """print."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """update"""
        if args:
            i = 0
            for item in args:
                if i == 0:
                    self.id = item
                if i == 1:
                    self.width = item
                if i == 2:
                    self.height = item
                if i == 3:
                    self.x = item
                if i == 4:
                    self.y = item
                i = i + 1
        if kwargs:
            for x, y in kwargs.items():
                if x == 'id':
                    self.id = y
                if x == 'width':
                    self.__width = y
                if x == 'height':
                    self.__height = y
                if x == 'x':
                    self.__x = y
                if x == 'y':
                    self.__y = y

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"x": self.x, "y": self.y, "id": self.id, "height": self.height,
                "width": self.width}
