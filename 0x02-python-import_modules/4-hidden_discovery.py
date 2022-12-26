#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    hid = dir(hidden_4)
    for func in hid:
        if not func.startswith("_"):
            print(func)
