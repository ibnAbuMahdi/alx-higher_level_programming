#!/usr/bin/python3
""" 10-student.py """
import json


class Student:
    """ student """

    def __init__(self, fn, ln, age):
        """ init method """
        self.first_name = fn
        self.last_name = ln
        self.age = age

    def to_json(self, attrs=None):
        """ to json """
        if isinstance(attrs, list) and isinstance(attrs[0], str):
            mdict = json.loads(json.dumps(self.__dict__))
            ndict = {}
            for att in attrs:
                if att in mdict:
                    ndict.update({att: att})
            return ndict
        else:
            return json.loads(json.dumps(self.__dict__))

    def reload_from_json(self, json):
        """ reload from json """
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
