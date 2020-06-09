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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        import json
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        y = json.dumps(list_dictionaries)
        return y

    @classmethod
    def save_to_file(cls, list_objs):
        import json
        filename = cls.__name__ + ".json"
        with open(filename, "w") as File:
            list = []
            if list_objs is not None:
                list = [item.to_dictionary() for item in list_objs]
            File.write(Base.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        import json
        y = json.loads(json_string)
        return y
