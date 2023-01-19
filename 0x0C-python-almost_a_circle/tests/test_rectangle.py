#!/usr/bin/python3
""" test_rectangle """
import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    """ Rectangle tests """

    def test_id_None(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(1,1,1,1)
        self.assertEqual(r2.id, 2)
        self.assertTrue(issubclass(Rectangle, Base))

    def test_id_not_None(self):
        r1 = Rectangle(4, 3, 0, 0, 3)
        self.assertEqual(r1.id, 3)

        r2 = Rectangle(3, 2, 1, 1, 8)
        self.assertEqual(r2.id, 8)

    def test_attributes_exist(self):
        r4 = Rectangle(3, 2, 4, 2, 9)
        self.assertTrue(hasattr(r4, "width"))
        self.assertEqual(r4.width, 3)

        self.assertTrue(hasattr(r4, "height"))
        self.assertEqual(r4.height, 2)

        self.assertTrue(hasattr(r4, "x"))
        self.assertEqual(r4.x, 4)

        self.assertTrue(hasattr(r4, "y"))
        self.assertEqual(r4.y, 2)
