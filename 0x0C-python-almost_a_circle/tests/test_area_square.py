#!/usr/bin/python3
import unittest
from unittest.mock import patch
from models.square import Square as R
from io import StringIO


class TestAreaRect(unittest.TestCase):

    def test_w_gt_h(self):
        r1 = R(4)
        self.assertEqual(r1.area(), 4 * 4)

    def test_display(self):
        r4 = R(2)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r4.display()
            self.assertEqual(fake_out.getvalue(), '##\n##\n')

        r6 = R(1)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r6.display()
            self.assertEqual(fake_out.getvalue(), '#\n')

    def test_print(self):
        r4 = R(3, 4, 9, 2)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r4)
            self.assertEqual(fake_out.getvalue(), '[Square] (2) 4/9 - 3\n')

        r5 = R(4, 4, 1, 15)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r5)
            self.assertEqual(fake_out.getvalue(), '[Square] (15) 4/1 - 4\n')

        r6 = R(1, 0, 0, 0)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r6)
            self.assertEqual(fake_out.getvalue(), '[Square] (0) 0/0 - 1\n')

    def test_display1(self):
        r4 = R(2, 0, 0)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r4.display()
            self.assertEqual(fake_out.getvalue(), '##\n##\n')

        r5 = R(2, 1, 1)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r5.display()
            self.assertEqual(fake_out.getvalue(), '\n ##\n ##\n')

        r6 = R(1,2,3)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r6.display()
            self.assertEqual(fake_out.getvalue(), '\n\n\n  #\n')

        r7 = R(3, 1, 0)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r7.display()
            self.assertEqual(fake_out.getvalue(), ' ###\n ###\n ###\n')
