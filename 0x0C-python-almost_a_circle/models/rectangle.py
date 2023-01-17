#!/usr/bin/python3
""" rectangle.py """
from models.base import Base as B


class Rectangle(B):
    """ the Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init """
        super().__init__(id)
        if isinstance(height, int):
            if height <= 0:
                raise ValueError('height must be > 0')
        else:
            raise TypeError('height must be an integer')

        if isinstance(width, int):
            if width <= 0:
                raise ValueError('width must be > 0')
        else:
            raise TypeError('width must be an integer')

        if isinstance(x, int):
            if x < 0:
                raise ValueError('x must be >= 0')
        else:
            raise TypeError('x must be an integer')

        if isinstance(y, int):
            if y < 0:
                raise ValueError('y must be >= 0')
        else:
            raise TypeError('y must be an integer')

        self.__width, self.__height, self.__x, self.__y = width, height, x, y

    @property
    def width(self):
        """ width """
        return self.__width

    @width.setter
    def width(self, val):
        if isinstance(val, int):
            if val <= 0:
                raise ValueError('width must be > 0')
            self.__width = val
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """ height """
        return self.__height

    @height.setter
    def height(self, val):
        if isinstance(val, int):
            if val <= 0:
                raise ValueError('height must be > 0')
            self.__height = val
        else:
            raise TypeError('height must be an integer')

    @property
    def x(self):
        """ x """
        return self.__x

    @x.setter
    def x(self, val):
        if isinstance(val, int):
            if val < 0:
                raise ValueError('x must be >= 0')
            self.__x = val
        else:
            raise TypeError('x must be an integer')

    @property
    def y(self):
        """ y """
        return self.__y

    @y.setter
    def y(self, val):
        if isinstance(val, int):
            if val < 0:
                raise ValueError('y must be >= 0')
            self.__y = val
        else:
            raise TypeError('y must be an integer')

    def area(self):
        """ area """
        return self.__width * self.__height

    def display(self):
        """ display rectangle with # """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" "*self.__x + "#"*self.__width)

    def __str__(self):
        """ string rectangle """
        string = "[Rectangle] ({}) {}/{} - \
{}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

        return string

    def update(self, *args, **kwargs):
        """ update square """
        if kwargs is not None and (args is None or len(args) == 0):
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.__width = v
                elif k == "height":
                    self.__height = v
                elif k == 'x':
                    self.__x = v
                elif k == 'y':
                    self.__y = v

        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.__width = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
        elif len(args) == 4:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
        elif len(args) >= 5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]

    def to_dictionary(self):
        """  return customized dict version of Rectangle """
        idict = self.__dict__
        odict = dict()

        for k, v in idict.items():
            if k == '_Rectangle__width':
                odict.update({'width': v})
            elif k == '_Rectangle__height':
                odict.update({'height': v})
            elif k == '_Rectangle__x':
                odict.update({'x': v})
            elif k == '_Rectangle__y':
                odict.update({'y': v})
            elif k == 'id':
                odict.update({'id': v})

        return odict
