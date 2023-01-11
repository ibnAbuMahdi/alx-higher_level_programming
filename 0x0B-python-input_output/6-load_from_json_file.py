#!/usr/bin/python3
""" 6-load_from_json_file.py """
import json


def load_from_json_file(filename):
    """ loads an object from json file """

    with open(filename, encoding="utf-8") as f:
        return json.load(f)
