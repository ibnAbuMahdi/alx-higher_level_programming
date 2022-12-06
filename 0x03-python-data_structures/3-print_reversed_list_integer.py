#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        ln = len(my_list)
        if ln > 0:
            ln *= -1
            i = -1
            while i >= ln:
                print("{:d}".format(my_list[i]))
                i -= 1
