#!/usr/bin/python3
""" Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_type(self):
        self.assertIsInstance(max_integer([1, 3, 5]), int)
    """
    def test_invalid_types(self):
        self.assertraises(KeyError, max_integer, {1:3, 3: 5})
        self.assertraises(TypeError, max_integer, 1023)
    """
    def test_equal(self):
        self.assertEqual(max_integer([1, 3, 5]), 5)

    def test_None(self):
        self.assertIsNone(max_integer([]))

    def test_notIntEqual(self):
        self.assertEqual(max_integer(['a', 'b']), 'b')

    def test_float(self):
        self.assertIsInstance(max_integer([3.2, 4.5, 6.8]), float)

if __name__ == '__main__':
    unittest.main()
