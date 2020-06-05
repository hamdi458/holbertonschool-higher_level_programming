#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)"""


def from_json_string(my_str):
    """function that returns the JSON representation of an object (string)"""
    import json
    y = json.loads(my_str)
    return y
