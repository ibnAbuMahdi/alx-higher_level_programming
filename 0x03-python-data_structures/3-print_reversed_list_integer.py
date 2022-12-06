#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    ln = len(my_list)
    if ln > 0:
        while ln - 1 >= 0:
            print("{:d}".format(my_list[ln - 1]))
            ln -= 1
