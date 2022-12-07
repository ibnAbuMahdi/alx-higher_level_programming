#!/usr/bin/python3
def print_sorted_dictionary(a_d):
    keys = sorted(a_d)
    for k in keys:
        print("{}: {}".format(k, a_d.get(k)))
