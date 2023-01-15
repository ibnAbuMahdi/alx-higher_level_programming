#!/usr/bin/python3
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle as R
from io import StringIO


class TestAreaRect(unittest.TestCase):

    def test_w_gt_h(self):
        r1 = R(4, 6)
        self.assertEqual(r1.area(), 4 * 6)

    def test_h_gt_w(self):
        r2 = R(6, 5)
        self.assertEqual(r2.area(), 5 * 6)

    def test_h_eq_w(self):
        r3 = R(5, 5)
        self.assertEqual(r3.area(), 5 * 5)

    def test_display(self):
        r4 = R(2, 3)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r4.display()
            self.assertEqual(fake_out.getvalue(), '##\n##\n##\n')

        r5 = R(2, 2)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r5.display()
            self.assertEqual(fake_out.getvalue(), '##\n##\n')

        r6 = R(1,1)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r6.display()
            self.assertEqual(fake_out.getvalue(), '#\n')

        r7 = R(4, 3)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r7.display()
            self.assertEqual(fake_out.getvalue(), '####\n####\n####\n')

    def test_print(self):
        r4 = R(2, 3, 4, 9, 2)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r4)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (2) 4/9 - 2/3\n')

        r5 = R(2, 2, 4, 1, 15)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r5)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (15) 4/1 - 2/2\n')

        r6 = R(1, 1, 0, 0, 0)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r6)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (0) 0/0 - 1/1\n')

    def test_display1(self):
        r4 = R(2, 3, 0, 0)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r4.display()
            self.assertEqual(fake_out.getvalue(), '##\n##\n##\n')

        r5 = R(2, 2, 1, 1)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r5.display()
            self.assertEqual(fake_out.getvalue(), '\n ##\n ##\n')

        r6 = R(1,1,2,3)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r6.display()
            self.assertEqual(fake_out.getvalue(), '\n\n\n  #\n')

        r7 = R(4, 3, 1, 0)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r7.display()
            self.assertEqual(fake_out.getvalue(), ' ####\n ####\n ####\n')
        r8 = R(4, 3, 0, 1)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r8.display()
            self.assertEqual(fake_out.getvalue(), '\n####\n####\n####\n')
