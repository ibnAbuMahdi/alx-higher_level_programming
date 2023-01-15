#!/usr/bin/python3
""" r1 """
import unittest
from models.rectangle import Rectangle as R


class TestRectangleValueType(unittest.TestCase):
    """ Tests for types and values """

    def test_width(self):
        ls = ["4", [4], {4}, (4,), {1:4}]
        for item in ls:
            with self.assertRaises(TypeError) as tm:
                R(item, 3, 2, 1, 2)
            exc = tm.exception
            self.assertEqual(str(exc), "width must be an integer")
        vals = [-4, 0]
        for num in vals:
            with self.assertRaises(ValueError) as cm:
                R(num, 3, 3, 1, 0)
            exc = cm.exception
            self.assertEqual(str(exc), "width must be > 0")

    def test_height(self):
        ls = ["4", [4], {4}, (4,), {1:4}]
        for item in ls:
            with self.assertRaises(TypeError) as tm:
                R(3, item, 2, 1, 2)
            exc = tm.exception
            self.assertEqual(str(exc), "height must be an integer")
        vals = [-4, 0]
        for num in vals:
            with self.assertRaises(ValueError) as cm:
                R(3, num, 3, 1, 0)
            exc = cm.exception
            self.assertEqual(str(exc), "height must be > 0")

    def test_x(self):
        ls = ["4", [4], {4}, (4,), {1:4}]
        for item in ls:
            with self.assertRaises(TypeError) as tm:
                R(4, 3, item, 1, 2)
            exc = tm.exception
            self.assertEqual(str(exc), "x must be an integer")
        vals = [-4, -50]
        for num in vals:
            with self.assertRaises(ValueError) as cm:
                R(5, 3, num, 1, 0)
            exc = cm.exception
            self.assertEqual(str(exc), "x must be >= 0")

    def test_y(self):
        ls = ["4", [4], {4}, (4,), {1:4}]
        for item in ls:
            with self.assertRaises(TypeError) as tm:
                R(6, 3, 2, item, 2)
            exc = tm.exception
            self.assertEqual(str(exc), "y must be an integer")
        vals = [-4, -60]
        for num in vals:
            with self.assertRaises(ValueError) as cm:
                R(3, 3, 1, num, 0)
            exc = cm.exception
            self.assertEqual(str(exc), "y must be >= 0")

