#!/usr/bin/python3
"""function that returns the dictionary description"""


def class_to_json(obj):
    """function that returns the dictionary description with simple data
structure (list, dictionary, string, integer and boolean) for JSON serialization
of an object:"""
    y = obj.__dict__
    return y
