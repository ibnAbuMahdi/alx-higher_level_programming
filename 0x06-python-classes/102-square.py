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

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.area() < other.area():
            return True
        else:
            return False
    
    def __gt__(self, other):
        if self.area() > other.area():
            return True
        else:
            return False
    
    def __ne__(self, other):
        if self.area() != other.area():
            return True
        else:
            return False
    
    def __ge__(self, other):
        if self.area() >= other.area():
            return True
        else:
            return False
    
    def __le__(self, other):
        if self.area() <= other.area():
            return True
        else:
            return False
