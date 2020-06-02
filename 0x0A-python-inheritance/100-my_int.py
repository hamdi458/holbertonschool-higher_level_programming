#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __eq__(self, value):
        """return true or false"""
        return self.real != value

    def __ne__(self, value):
        """return true or false"""
        return int(self) == int(other)
