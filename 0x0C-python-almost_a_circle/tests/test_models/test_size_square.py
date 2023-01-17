#!/usr/bin/python3
from io import StringIO
from models.square import Square as S
from unittest import TestCase
from unittest.mock import patch


class TestSizeSquare(TestCase):

    def test_valid_size(self):      
        r4 = S(3, 4, 9, 2)
        r4.size = 5
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r4)
            self.assertEqual(fake_out.getvalue(), '[Square] (2) 4/9 - 5\n')

        r5 = S(4, 4, 1, 15)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r5.size = 10
            print(r5.size)
            self.assertEqual(fake_out.getvalue(), '10\n')

    def test_invalid_size(self):
        ls = ["4", 5.0, [4], {4}, (4,), {1:4}]
        s1 = S(10)       
        for item in ls:
            with self.assertRaises(TypeError) as tm:
                s1.size = item
            exc = tm.exception
            self.assertEqual(str(exc), "width must be an integer")
        vals = [-4, 0]
        for num in vals:
            with self.assertRaises(ValueError) as cm:
                s1.size = num
            exc = cm.exception
            self.assertEqual(str(exc), "width must be > 0")

    def test_width_height(self):
        r6 = S(1, 0, 0, 0)
        r6.size = 3
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r6.width)
            print(r6.height)
            self.assertEqual(fake_out.getvalue(), '3\n3\n')
