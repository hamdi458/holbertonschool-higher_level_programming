#!/usr/bin/python3
"""class base"""


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialise id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        import json
        if list_dictionaries == None or  list_dictionaries == []:
            return []
        y = json.dumps(list_dictionaries)
        return y
