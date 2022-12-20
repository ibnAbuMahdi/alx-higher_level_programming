#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (IndexError, TypeError,
            NameError, ZeroDivisionError, ValueError) as ex:
        print("Exception:", ex, file=sys.stderr)
        return None
