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
