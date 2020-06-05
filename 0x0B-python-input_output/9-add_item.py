#!/usr/bin/python3
"""script that adds all arguments to a Python list, and then save them to a file
"""


import sys


if __name__ == "__main__":
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
    try:
        item_json = load_from_json_file("add_item.json")
    except:
        item_json = []
    for item in sys.argv[1:]:
        item_json.append(item)
    save_to_json_file(item_json, "add_item.json")
