#!/usr/bin/python3
""" 0-read_file.py """


def read_file(filename=""):
    """ reads a file content and prints it out """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
