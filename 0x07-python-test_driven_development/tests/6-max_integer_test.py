#!/usr/bin/python3

"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        actual = max_integer([1, 2, 3, 4])
        expected = 4
        self.assertEqual(actual, expected)

        actual = max_integer([])
        expected = None
        self.assertEqual(actual, expected)

        actual = max_integer([3])
        expected = 3
        self.assertEqual(actual, expected)

        with self.assertRaises(TypeError):
            max_integer({1, 2, 3})

        actual = max_integer({0: 32, 1: 54})
        expected = 54
        self.assertEqual(actual, expected)

        with self.assertRaises(TypeError):
            max_integer({0: 32, 1: "54"})

        with self.assertRaises(TypeError):
            max_integer(0, 11, 32, 26, 54, 3)

        actual = max_integer((0, 11, 32, 3, 24))
        expected = 32
        self.assertEqual(actual, expected)

        actual = max_integer(['1', '45', '32', '0'])
        expected = '45'
        self.assertEqual(actual, expected)

        actual = max_integer("1, 2, 3, 3, 4")
        expected = '4'
        self.assertEqual(actual, expected)

        actual = max_integer("1, 22, 83, 93, 14")
        expected = '9'
        self.assertEqual(actual, expected)

        actual = max_integer("a, b, c, d, g, s")
        expected = 's'
        self.assertEqual(actual, expected)

        actual = max_integer([[2], [34], [23]])
        expected = [34]
        self.assertEqual(actual, expected)

        actual = max_integer([2.344, 54.098, 76.763, 0.678, 11.0])
        expected = 76.763
        self.assertEqual(actual, expected)

        actual = max_integer([2.344, 54.098, 76.763, 0.678, float("nan")])
        expected = 76.763
        self.assertEqual(actual, expected)

        actual = max_integer([2.344, 54.098, 76.763, 0.678, float("inf")])
        expected = float("inf")
        self.assertEqual(actual, expected)

        actual = max_integer()
        expected = None
        self.assertEqual(actual, expected)

        actual = max_integer([34, 1, -3])
        expected = 34
        self.assertEqual(actual, expected)
