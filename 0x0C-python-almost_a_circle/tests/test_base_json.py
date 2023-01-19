#!/usr/bin/python3
from unittest import TestCase
from models.base import Base as B
from models.rectangle import Rectangle as R
from models.square import Square as S
from io import StringIO
import json
from unittest.mock import patch


class TestJSONBase(TestCase):

    def test_None(self):
        self.assertEqual(B.to_json_string(None), "[]")
        self.assertEqual(B.to_json_string([]), "[]")
        ins = ['str', (1,), {1}, {0:1}, 1.2, 1j]
        for inp in ins:
            self.assertEqual(B.to_json_string(inp), "[]")

    def test_not_None(self):
        self.assertEqual(B.to_json_string([{'x': 0, 'y': 1}]), '[{"x": 0, "y": 1}]')
        dcts = [{'x': 1, 'width': 4}, {'y': 8, 'height': 3}]
        dcts_s = '[{"x": 1, "width": 4}, {"y": 8, "height": 3}]'

        self.assertEqual(B.to_json_string(dcts), dcts_s)

        dcts = [{'x': 1, 'width': 4}, "not a dict!", {'y': 8, 'height': 3}]
        dcts_s = '[{"x": 1, "width": 4}, {"y": 8, "height": 3}]'

        self.assertEqual(B.to_json_string(dcts), dcts_s)

    def test_save_none(self):
        try:
            R.save_to_file(None)
            with open('Rectangle.json', encoding="utf-8") as f:
                cont = f.read()
                self.assertEqual(cont, "[]")
        except FileNotFoundError:
            print("file not found")

    def test_save_empty(self):
        try:
            R.save_to_file([])
            with open('Rectangle.json', encoding="utf-8") as f:
                cont = f.read()
                self.assertEqual(cont, "[]")
        except FileNotFoundError:
            print("file not found")

    def test_save_rect_not_none(self):
        try:
            R.save_to_file([R(3, 4)])                                           
            with open('Rectangle.json', encoding="utf-8") as f:
                cont = f.read()
                self.assertTrue('"x": 0' in cont and  '"y": 0' in cont and '"height": 4' in cont and '"width": 3' in cont and '"id": 1' in cont) 
        except FileNotFoundError:
            print("file not found")

        try:
            R.save_to_file([R(5, 6, 1, 1), R(7, 8, 2, 2)])                                           
            with open('Rectangle.json', encoding="utf-8") as f:
                cont = f.read()
                self.assertTrue('"x": 1' in cont and  '"y": 1' in cont and '"height": 6' in cont and '"width": 5' in cont and '"id": 2' in cont) 
                self.assertTrue('"x": 2' in cont and  '"y": 2' in cont and '"height": 8' in cont and '"width": 7' in cont and '"id": 3' in cont) 
        
        except FileNotFoundError:
            print("file not found")

        try:
            R.save_to_file([R(5, 9, 1, 1), "not_obj", R(7, 8, 2, 2)])                                           
            with open('Rectangle.json', encoding="utf-8") as f:
                cont = f.read()
                self.assertTrue('"x": 1' in cont and  '"y": 1' in cont and '"height": 9' in cont and '"width": 5' in cont and '"id": 4' in cont) 
                self.assertTrue('"x": 2' in cont and  '"y": 2' in cont and '"height": 8' in cont and '"width": 7' in cont and '"id": 5' in cont) 
        
        except FileNotFoundError:
            print("file not found")


    def test_save_rect_not_none(self): 
        try:
            S.save_to_file([S(3)])                                           
            with open('Square.json', encoding="utf-8") as f:
                cont = f.read()
                self.assertTrue('"x": 0' in cont and  '"y": 0' in cont and '"size": 3' in cont and '"id": 1' in cont) 
        except FileNotFoundError:
            print("file not found")

        try:
            S.save_to_file([S(6, 1, 1), S(7, 2, 2)])                                           
            with open('Square.json', encoding="utf-8") as f:
                cont = f.read()
                self.assertTrue('"x": 1' in cont and  '"y": 1' in cont and '"size": 6' in cont and '"id": 2' in cont) 
                self.assertTrue('"x": 2' in cont and  '"y": 2' in cont and '"size": 7' in cont and '"id": 3' in cont) 
        
        except FileNotFoundError:
            print("file not found")

        try:
            S.save_to_file([S(9, 1, 1), "not_obj", S(8, 2, 2)])          
            with open('Square.json', encoding="utf-8") as f:
                cont = f.read()
                self.assertTrue('"x": 1' in cont and  '"y": 1' in cont and '"size": 9' in cont and '"id": 4' in cont) 
                self.assertTrue('"x": 2' in cont and  '"y": 2' in cont and '"size": 8' in cont and '"id": 5' in cont) 
        
        except FileNotFoundError:
            print("file not found")

    def test_not_list(self):
        try:
            R.save_to_file("not_list")      
            with open('Rectangle.json', encoding="utf-8") as f:
                cont = f.read()
                self.assertEqual(cont, "[]")
        except FileNotFoundError:
            print("file not found")
