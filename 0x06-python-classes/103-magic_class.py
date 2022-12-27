#!/usr/bin/python3
""" A module for a class that does magic """


class MagicClass:
    """ where the magic happens """

    def __init__(self, radius=0):
        """ the init method """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ returns the area """
        return self.__radius**2 * math.pi

    def circumference(self):
        """ returns the circumference """
        return 2 * math.pi * self.__radius
