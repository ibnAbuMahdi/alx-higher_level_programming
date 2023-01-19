#!/usr/bin/python3
""" test_rectangle """
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    """ Rectangle tests """

    def test_id_None(self):
        r1 = Square(3)
        self.assertEqual(r1.id, 1)
        r2 = Square(1,1,1)
        self.assertEqual(r2.id, 2)
        self.assertTrue(issubclass(Square, Rectangle))

    def test_id_not_None(self):
        r1 = Square(3, 0, 0, 5)
        self.assertEqual(r1.id, 5)

        r2 = Square(2, 1, 1, 8)
        self.assertEqual(r2.id, 8)

    def test_attributes_exist(self):
        r4 = Square(2, 4, 2, 9)
        self.assertTrue(hasattr(r4, "width"))
        self.assertEqual(r4.width, 2)

        self.assertTrue(hasattr(r4, "height"))
        self.assertEqual(r4.height, 2)

        self.assertTrue(hasattr(r4, "x"))
        self.assertEqual(r4.x, 4)

        self.assertTrue(hasattr(r4, "y"))
        self.assertEqual(r4.y, 2)
