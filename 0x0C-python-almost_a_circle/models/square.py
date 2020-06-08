#!/usr/bin/python3
"""class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize constructor"""
        super().__init__(size, size, x, y, id)
    def __str__(self):
        """str"""
        return '[Square] ({}) {}/{} - {}' .format(self.id, self.x, self.y,
                                                  self.width)

    @property
    def size(self):
        """Get size."""
        return self.height

    @size.setter
    def size(self, valeur):
        """ set size"""
        self.width = valeur
        self.height = valeur

    def update(self, *args, **kwargs):
        """update"""
        i = 0
        if args:
            for item in args:
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
                i = i + 1
        if kwargs:
            for x, y in kwargs.items():
                if x == 'id':
                    self.id = y
                if x == "size":
                    self.width = y
                    self.height = y
                if x == 'x':
                    self.x = y
                if x == 'y':
                    self.y = y
