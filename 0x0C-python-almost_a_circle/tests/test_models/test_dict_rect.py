#!/usr/bin/python3
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle as R
from io import StringIO


class TestDictRectangle(unittest.TestCase):

    def test_update_args(self):
        r1 = R(5, 5, 5, 5)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (1) 5/5 - 5/5\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update()
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (1) 5/5 - 5/5\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update(76)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (76) 5/5 - 5/5\n')

        with patch('sys.stdout', new = StringIO()) as fake_out:                          
            r1.update(76, 8)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (76) 5/5 - 8/5\n')

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

    def test_update_dict(self):
        r1 = R(5, 5, 5, 5)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (2) 5/5 - 5/5\n')
        rtemp = R(3, 3)
        rd = rtemp.to_dictionary()
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update(**rd)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (3) 0/0 - 3/3\n')
        rtemp = R(4, 6, 3)
        rd = rtemp.to_dictionary()
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.update(**rd)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (4) 3/0 - 4/6\n')
        rtemp = R(3, 8, 2, 1)
        rd = rtemp.to_dictionary()
        with patch('sys.stdout', new = StringIO()) as fake_out:                          
            r1.update(**rd)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (5) 2/1 - 3/8\n')
        rtemp = R(8, 2, 2, 1, 3)
        rd = rtemp.to_dictionary()
        with patch('sys.stdout', new = StringIO()) as fake_out:                              
            r1.update(**rd)
            print(r1)
            self.assertEqual(fake_out.getvalue(), '[Rectangle] (3) 2/1 - 8/2\n')






















