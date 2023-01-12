#!/usr/bin/python3
""" 100-append_after.py """


def append_after(fn="", search="", new=""):
    """ append new after line with search """

    apps = []
    with open(fn, "r+", encoding="utf-8") as f:
        for line in f:
            apps.append(line)
            if search in line:
                apps.append(new)

    with open(fn, "w", encoding="utf-8") as f:
        f.writelines(apps)
