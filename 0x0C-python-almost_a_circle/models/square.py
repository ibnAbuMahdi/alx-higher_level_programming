#!/usr/bin/python3
""" square """
from models.rectangle import Rectangle as R


class Square(R):
    """ the square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ the init method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str """
        string = "[Square] ({}) {}/{} - \
{}".format(self.id, self.x, self.y, self.width)
        return string

    @property
    def size(self):
        """ size """
        return self.width

    @size.setter
    def size(self, val):
        if isinstance(val, int):
            if val <= 0:
                raise ValueError('width must be > 0')
            self.__width = val
            self.__height = val
        else:
            raise TypeError('width must be an integer')
