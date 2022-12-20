#!/usr/bin/python3

import sys


def safe_print_integer_err(v):
    try:
        print("{:d}".format(v))
        return True
    except (TypeError, ValueError) as ex:
        print("Exception:", ex, file=sys.stderr)
        return False
