#!/usr/bin/python3
""" 2-append_write.py """


def append_write(filename="", text=""):
    """ appends text to a file with name filename """
    
    n = 0
    with open(filename, "a", encoding="utf-8") as f:
            n = f.write(text)
    return n 
