#!/usr/bin/python3
""" 3-say_my_name.py """


def say_my_name(fn, ln=""):
    """ prints the first and last name provided """

    if type(fn) is not str:
        raise TypeError('first_name must be a string')
    if type(ln) is not str:
        raise TypeError('last_name must be a string')

    if len(ln) > 0:
        print("My name is {} {}".format(fn, ln))
