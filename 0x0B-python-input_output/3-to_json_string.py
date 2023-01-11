#!/usr/bin/python3
""" 3-to_json_string.py """
import json


def to_json_string(my_obj):
    """ returns json repr of my_obj """
    return json.dumps(my_obj)
