#!/usr/bin/python3
""" 101-add_attribute.py """


def add_attribute(obj=None, nm=None, val=None):
    """ add an attribute to obj if possible """

    if not isinstance(nm, str) or len(nm) == 0:
        raise TypeError('can\'t add new attribute')
    if obj is None or isinstance(obj,
                                 (str, int, dict, tuple, set, float, complex)):
        raise TypeError('can\'t add new attribute')
    if hasattr(obj, '__slots__') and nm not in obj.__slots__:
        raise TypeError('can\'t add new attribute')
    setattr(obj, nm, val)
