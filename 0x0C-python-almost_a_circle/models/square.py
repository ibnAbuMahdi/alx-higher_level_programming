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
            self.width = val
            self.height = val
        else:
            raise TypeError('width must be an integer')

    def update(self, *args, **kwargs):
        """ update Square instance """
        if kwargs is not None and (args is None or len(args) == 0):
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.size = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
        elif len(args) >= 4:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]

    def to_dictionary(self):
        """  return customized dict version of Square """
        idict = self.__dict__
        odict = dict()

        for k, v in idict.items():
            if k == '_Rectangle__width':
                odict.update({'size': v})
            elif k == '_Rectangle__x':
                odict.update({'x': v})
            elif k == '_Rectangle__y':
                odict.update({'y': v})
            elif k == 'id':
                odict.update({'id': v})

        return odict
