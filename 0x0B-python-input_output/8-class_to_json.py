#!/usr/bin/python3
""" 8-class_to_json.py """
import json


def class_to_json(obj):
    """ converts a class to json string """

    return json.loads(json.dumps(obj.__dict__))
