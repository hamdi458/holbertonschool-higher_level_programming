#!/usr/bin/python3
"""creates an Object from a JSON file"""


def load_from_json_file(filename):
    """ creates an Object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as file:
        import json
        y = json.load(file)
        return y
