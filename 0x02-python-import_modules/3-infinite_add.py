#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    ln = len(argv) - 1
    if ln == 0:
        print("0")
    elif ln > 0:
        sm = 0
        for i in range(ln):
            sm += int(argv[i + 1])
        print("{}".format(sm))
