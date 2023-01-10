#!/usr/bin/python3
""" 0-lookup.py """


def lookup(obj):
    """ returns the available attributes of obj """

    return list(dir(obj))
