#!/usr/bin/python3
""" locked class """


class LockedClass:
    __slots__ = ["first_name"]

    def __init__(self, name=None):
        if name is not None:
            self.first_name = name
