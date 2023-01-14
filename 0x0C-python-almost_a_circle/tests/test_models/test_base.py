#!/usr/bin/python3
""" base.py """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ base class tests """

    def test_nb_object_private(self):
        b1 = Base()
        self.assertFalse(hasattr(b1, "nb_objects"))
        self.assertFalse(hasattr(b1, "__nb_objects"))

    def test_None(self):
        b2 = Base()
        self.assertIsNotNone(b2.id)
        self.assertEqual(b2.id, 1)

    def test_id_not_None(self):
        b3 = Base(4)
        self.assertIsNotNone(b3.id)
        self.assertEqual(b3.id, 4)
        id3 = b3.id
        b4 = Base()
        self.assertNotEqual(b4.id, id3 + 1)
        b5 = Base()
        self.assertGreater(b5.id, b4.id)

    def test_neg_to_pos(self):
        b6 = Base(-5)
        b7 = Base(0)
        b8 = Base(10)
        self.assertEqual(b6.id, -5)
        self.assertEqual(b7.id, 0)
        self.assertEqual(b8.id, 10)
