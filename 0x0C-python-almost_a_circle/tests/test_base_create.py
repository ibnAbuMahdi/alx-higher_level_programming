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
        self.assertTrue(isinstance(R.create(**(r1.to_dictionary())), R))

        self.assertFalse(R.create(**(r1.to_dictionary())) is r1)
        self.assertFalse(R.create(**(r1.to_dictionary())) == r1)

    def test_Square(self):                                                        
        r1 = S(3,5)
        self.assertTrue(isinstance(S.create(**(r1.to_dictionary())), S))

        self.assertFalse(S.create(**(r1.to_dictionary())) is r1)
        self.assertFalse(S.create(**(r1.to_dictionary())) == r1)
