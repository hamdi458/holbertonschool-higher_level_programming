#!/usr/bin/python3
"""inherited of class MyList."""


class MyList(list):
    """class mylist"""
    def print_sorted(self):
        """Print"""
        print(sorted(self))
