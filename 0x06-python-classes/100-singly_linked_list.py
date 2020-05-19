#!/usr/bin/python3
"""class singly-linked list."""


class Node:
    """class node"""

    def __init__(self, data, next_node=None):
        """Initialize a Node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """set data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """get the next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """wiw"""
        if value is not None and value is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value
