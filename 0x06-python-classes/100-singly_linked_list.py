#!/usr/bin/python3
"""class singly-linked-list"""


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
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Define class_ """
    def __init__(self):
        """cons """
        self.__head = None

    def __str__(self):
        """str """
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp.data)
            string += "\n"
            tmp = tmp.next_node
        string = string[:-1]
        return string

    def sorted_insert(self, value):
        """sorted list"""
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node
