#!/usr/bin/python3
import unittest
from unittest.mock import patch
from models.square import Square as R
from io import StringIO


class TestUpdateRectangle(unittest.TestCase):

    def test_update_args(self):
        r1 = R(5, 5, 5)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Square] (1) 5/5 - 5\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update()
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Square] (1) 5/5 - 5\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update(76)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Square] (76) 5/5 - 5\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:                          
            r1.update(76, 8)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Square] (76) 5/5 - 8/5\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:                              
            r1.update(76, 8, 4)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (76) 5/5 - 8/4\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:                              
            r1.update(76, 7, 3, 2)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (76) 2/5 - 7/3\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update(52, 9, 2, 3, 8)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (52) 3/8 - 9/2\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update(76, 3, 2, 8, 9, 3)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (76) 8/9 - 3/2\n')

    def test_update_kwargs(self):
        r1 = R(5, 5, 5, 5)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (2) 5/5 - 5/5\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update()
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (2) 5/5 - 5/5\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update(height=76)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (2) 5/5 - 5/76\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:                          
            r1.update(x=6, height=8)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (2) 6/5 - 5/8\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:                              
            r1.update(y=6, height=8, x=4)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (2) 4/6 - 5/8\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:                              
            r1.update(width=6, height=7, x=3, y=2)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (2) 3/2 - 6/7\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update(x=5, y=9, width=2, height=3, id=8)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (8) 5/9 - 2/3\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update(76, x=89, id=5)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (76) 5/9 - 2/3\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update(x=5, y=9, width=2, height=3, id=8, fake=7)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (8) 5/9 - 2/3\n')


