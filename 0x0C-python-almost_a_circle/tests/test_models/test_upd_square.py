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
            self.assertEqual(fake_out.getvalue(), '[Square] (76) 5/5 - 8\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:                              
            r1.update(76, 7, 3)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Square] (76) 3/5 - 7\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update(52, 9, 2, 3)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Square] (52) 2/3 - 9\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update(76, 3, 2, 8, 9, 3)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Square] (76) 2/8 - 3\n')

    def test_update_kwargs(self):
        r1 = R(5, 5, 5)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Square] (2) 5/5 - 5\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update()
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Square] (2) 5/5 - 5\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update(size=76)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Square] (2) 5/5 - 76\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:                          
            r1.update(x=6, size=8)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Square] (2) 6/5 - 8\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:                              
            r1.update(y=6, size=8, x=4)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Square] (2) 4/6 - 8\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:                              
            r1.update(width=6, height=7, x=3, y=2)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Square] (2) 3/2 - 8\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update(x=5, y=9, width=2, height=3, id=8)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Square] (8) 5/9 - 8\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update(76, x=89, id=5)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Square] (76) 5/9 - 8\n')



