#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    ln = len(argv) - 1
    if ln == 0:
        print("0 arguments.")
    elif ln > 0:
        if ln == 1:
            print("{} argument:".format(ln))
        elif ln > 1:
            print("{} arguments:".format(ln))
        for i in range(ln):
            print("{}: {}".format(i + 1, argv[i + 1]))
