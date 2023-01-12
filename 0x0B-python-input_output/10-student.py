#!/usr/bin/python3
""" 10-student.py """


class Student:
    """ student """

    def __init__(self, fn, ln, age):
        """ init method """
        self.first_name = fn
        self.last_name = ln
        self.age = age

    def to_json(self, attrs=None):
        """ to json """
        if isinstance(attrs, list) and len(attrs) > 0 and isinstance(attrs[0], str):
            mdict = self.__dict__
            ndict = {}
            for att in attrs:
                if att in mdict:
                    ndict.update({att: mdict[att]})
            return ndict
        else:
            return self.__dict__
