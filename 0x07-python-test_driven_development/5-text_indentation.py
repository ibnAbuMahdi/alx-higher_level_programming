#!/usr/bin/python3
""" 5-text_indentation.py """


def text_indentation(text):
    """ indents a text """

    if type(text) is not str:
        raise TypeError('text must be a string')

    prev = "."
    for c in text:
        if c == " " and (prev == "." or prev == "?" or prev == ":"):
            continue
        if c == "." or c == "?" or c == ":":
            prev = c
            print("{}\n".format(c))
        else:
            print(c, end="")
            prev = c

