#!/usr/bin/python3
""" This is a module for the class square """


class Square:
    """ class of a square
    """
    __size = 0
    def __init__(self, size):
        """the init method

        Args:
            size (int): the size of the square
        """
        self.__size = size
