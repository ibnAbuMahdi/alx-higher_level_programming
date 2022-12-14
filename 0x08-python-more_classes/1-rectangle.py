#!/usr/bin/python3
""" 0-rectangle.py """


class Rectangle:
    """ The Rectangle class """

    def __init__(self, width=0, height=0):
        """ intialize Rectangle with optional height and width """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')

        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Returns the width of the Rectangle """
        return self.__width

    @width.setter
    def width(self, val):
        """ sets the value of width to val """
        if type(val) is not int:
            raise TypeError('width must be an integer')
        if val < 0:
            raise ValueError('width must be >= 0')

        self.__width = val

    @property
    def height(self):
        """ Returns the height of the Rectangle """
        return self.__height

    @height.setter
    def height(self, val):
        """ sets the value of height to val """
        if type(val) is not int:
            raise TypeError('height must be an integer')
        if val < 0:
            raise ValueError('height must be >= 0')

        self.__height = val
