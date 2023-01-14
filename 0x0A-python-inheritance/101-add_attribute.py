#!/usr/bin/python3
""" 101-add_attribute.py """


def add_attribute(obj=None, name=None, val=None):
    """ add an attribute to obj if possible """

    if not isinstance(name, str) or len(name) == 0:
        raise TypeError('can\'t add new attribute')
    if obj is None or isinstance(obj,
                                 (str, int, dict, tuple, set, float, complex)):
        raise TypeError('cant\'t add new attribute')
    obj.name = val
