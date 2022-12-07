#!/usr/bin/python3
def simple_delete(a_d, key=""):
    if key in a_d.keys():
        a_d.pop(key)
    return a_d
