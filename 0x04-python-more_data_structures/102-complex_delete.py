#!/usr/bin/python3
def complex_delete(a_d, value):
    temp = a_d.copy()
    for k, v in temp.items():
        if value == v:
            a_d.pop(k)
    return a_d
