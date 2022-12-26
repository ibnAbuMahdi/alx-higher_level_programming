#!/usr/bin/python3

""" module for the square class """


class Square:
    """ The square class and all its fields """
    def __init__(self, size=0, pos=(0, 0)):

        """ the init method """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if self.isTuple(pos):
            self.__pos = pos
        else:
            raise TypeError("position must be a tuple of 2 \
positive integers")

    def area(self):
        """int: the area of the square """
        return self.__size**2

    @property
    def size(self):
        """ the object size getter """
        return self.__size

    @size.setter
    def size(self, val):
        if type(val) is not int:
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = val

    @property
    def position(self):
        """ the tuple of the position """
        return self.__pos

    @position.setter
    def position(self, val):
        if self.isTuple(val):
            self.__pos = val
        else:
            raise TypeError("position must be a tuple \
of 2 positive integers")

    def my_print(self):
        """ prints the square using # """
        if self.__size > 0:
            if self.__pos[1] > 0:
                print(" "*(self.__pos[1] - 1))
            for i in range(self.__size):
                print(" "*self.__pos[0] + "#"*self.__size)
        else:
            print("")

    def isTuple(self, val):
        """ check whether val is the right tuple """

        if type(val) is not tuple:
            return False
        if len(val) != 2:
            return False
        if type(val[0]) is not int or type(val[1]) is not int:
            return False
        if val[0] < 0 or val[1] < 0:
            return False
        return True





