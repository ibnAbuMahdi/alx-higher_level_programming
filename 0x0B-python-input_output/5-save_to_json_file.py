#!/usr/bin/python3
""" 5-save_to_json_file.py """
import json


def save_to_json_file(my_obj, filename):
    """ save my_obj to json file """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
