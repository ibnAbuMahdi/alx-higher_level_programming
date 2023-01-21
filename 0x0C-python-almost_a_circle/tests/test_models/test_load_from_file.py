#!/usr/bin/python3
from unittest import TestCase
from models.base import Base as B
from models.rectangle import Rectangle as R
from models.square import Square as S
from io import StringIO
import json
from unittest.mock import patch


class TestCreateBase(TestCase):

    def test_Rect(self):
        r1 = R(3,5)
        r2 = R(5, 2, 5, 2)
        R.save_to_file([r1, r2])
        out = R.load_from_file()
        for ins in out:
            self.assertTrue(isinstance(ins, R))

            self.assertFalse(ins is r1)
            self.assertFalse(ins == r1)

    def test_Square(self):
        r1 = S(3,5)
        r2 = S(5, 2, 5, 2)
        S.save_to_file([r1, r2])
        out = S.load_from_file()
        for ins in out:
            self.assertTrue(isinstance(ins, S))        

            self.assertFalse(ins is r1)  
            self.assertFalse(ins == r1) 

    def test_Rect_csv(self):
        r1 = R(3,5)
        r2 = R(5, 2, 5, 2)
        R.save_to_file_csv([r1, r2])
        out = R.load_from_file_csv()
        for ins in out:
            self.assertTrue(isinstance(ins, R))

            self.assertFalse(ins is r1)
            self.assertFalse(ins == r1)

    def test_Square_csv(self):
        r1 = S(3,5)
        r2 = S(5, 2, 5, 2)
        S.save_to_file_csv([r1, r2])
        out = S.load_from_file_csv()
        for ins in out:
            self.assertTrue(isinstance(ins, S))        

            self.assertFalse(ins is r1)  
            self.assertFalse(ins == r1) 

