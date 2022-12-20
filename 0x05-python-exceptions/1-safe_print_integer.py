#!/usr/bin/python3

def safe_print_integer(val):
    try:
        print("{:d}".format(val))
    except ValueError:
        return False
    else:
        return True
