#!/usr/bin/python3
""" 9-student.py """


class Student:
    """ student """

    def __init__(self, fn, ln, age):
        """ init method """
        self.first_name = fn
        self.last_name = ln
        self.age = age

    def to_json(self):
        """ to json """
        return self.__dict__
