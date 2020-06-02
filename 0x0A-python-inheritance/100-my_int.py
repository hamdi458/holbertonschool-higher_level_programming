#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __eq__(self, intnum):
        """return true or false"""
        return self.real != intnum

    def __ne__(self, intnum):
        """return true or false"""
        return self.real == intnum
