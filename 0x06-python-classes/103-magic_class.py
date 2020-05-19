#!/usr/bin/python3
""" magic class """
import math


class MagicClass:
    """ Magic Class """

    def __init__(self, radius=0):
        """ initialize a circle """

        self.__radius = 0
        if type(radius) is int and type(radius) is float:
            self.__radius = radius
        else:
            raise TypeError('radius must be a number')

    def area(self):
        """returns the area"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ returns the circumference"""
        return 2 * math.pi * self.__radius
