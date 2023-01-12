#!/usr/bin/python3
""" 1-write_file.py """


def write_file(filename="", text=""):
    """ writes text to a file with name filename """

    n = ""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    with open(filename, encoding="utf-8") as f:
        n = f.read()
    return len(n)
