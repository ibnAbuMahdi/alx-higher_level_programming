#!/usr/bin/python3
""" 2-is_same_class.py """


def is_same_class(obj, a_c):
    """ check whether obj is same class as a_c """

    if type(obj) == a_c:
        return True
    else:
        return False
