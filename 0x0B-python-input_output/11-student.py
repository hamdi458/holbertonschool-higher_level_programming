#!/usr/bin/python3
"""Class Student"""


class Student:
    """Class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initilize attribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dict"""
        return dict(self.__dict__)
