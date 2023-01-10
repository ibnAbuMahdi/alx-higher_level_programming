#!/usr/bin/python3
""" 4-inherits_from.py """


def inherits_from(obj, cl):
    """ check for inheritance """

    if issubclass(type(obj), cl) and type(obj) != cl:
        return True
    else:
        return False
