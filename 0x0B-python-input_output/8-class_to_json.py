#!/usr/bin/python3
""" 8-class_to_json.py """


def class_to_json(obj):
    """ converts a class to json string """

    return obj.__dict__
