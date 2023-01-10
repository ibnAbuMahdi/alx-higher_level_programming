#!/usr/bin/python3
""" 3-is_kind_of_class.py """


def is_kind_of_class(obj, a_c):
    """ checks if obj is kind of class """

    if isinstance(obj, a_c):
        return True
    else:
        return False
