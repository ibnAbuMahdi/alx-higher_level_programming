#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    ln = len(my_list)
    ln *= -1
    i = -1
    while i >= ln:
        print("{:d}".format(my_list[i]))
        i -= 1
