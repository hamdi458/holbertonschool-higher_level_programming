#!/usr/bin/python3
"""test class"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class Test"""
    def test_max_integer_1(self):
        i = [1, 2, 3, 4]
        self.assertEqual(max_integer(i), 4)

    def tes_max_integer_2(self):
        j = [1, 0, 5, 4]
        self.assertEqual(max_integer(j), 5)

    def test_max_integer_3(self):
        k = [5]
        self.assertEqual(max_integer(k), 5)

    def test_max_integer_empty(self):
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_string_empty(self):
        self.assertEqual(max_integer(""), None)

    def test_list_of_strings(self):
        ch = ["a", "b", "c", "d"]
        self.assertEqual(max_integer(ch), "d")

     def test_max_intger_neg(self):
        neg = [-10, -5, -4, 0]
        self.assertEqual(max_integer(neg), 0)

    def test_max_string(self):
        ch = "abcd"
        self.assertEqual(max_integer(ch), 'd')

     def test_max_integer_4(self):
         max = [4, 3, 2, 1]
         self.assertEqual(max_integer(max), 4)
