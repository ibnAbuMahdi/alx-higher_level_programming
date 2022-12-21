#!/usr/bin/python3

""" module for the square class """


class Square:
    """ The square class and all its fields """
    def __init__(self, size=0):

        """ the init method """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """int: the area of the square """
        return self.__size**2
