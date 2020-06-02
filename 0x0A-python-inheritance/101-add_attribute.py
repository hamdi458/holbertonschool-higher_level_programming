#!/usr/bin/python3
"""function"""


def add_attribute(object, attribut, valeur):
    """adds a new attribute to an object if its possible"""
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(object, attribut, valeur)
