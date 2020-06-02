#!/usr/bin/python3
"""class and inherited"""


def is_kind_of_class(obj, a_class):
    """Check object """
    if isinstance(obj, a_class):
        return True
    return False
