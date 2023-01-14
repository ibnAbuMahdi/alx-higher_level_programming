#!/usr/bin/python3
""" 100-my_int.py """


class MyInt(int):
    """ A rebel int class """

    def __init__(self, val=None):
        """ init """
        self.__val = val

    def __eq__(self, other):
        """ eq """
        if isinstance(other, MyInt):
            if self.__val == other.__val:
                return False
            return True
        if self.__val == other:
            return False
        return True

    def __ne__(self, other):
        """ ne """
        if isinstance(other, MyInt):
            if self.__val != other.__val:
                return False
            return True
        if self.__val != other:
            return False
        return True

    def __str__(self):
        """ str """
        if self.__val is not None:
            return str(self.__val)
