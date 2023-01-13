#!/usr/bin/python3
""" 6-base_geometry.py """


class BaseGeometry:
    """ Base Geometry """

    def area(self):
        """ area """
        raise Exception('area() is not implemented')

    def integer_validator(self, name="", value=""):
        """ int val """
        if len(name) == 0 and isinstance(value, str) and len(value) == 0:
            raise TypeError('integer_validator() missing 2 required \
positional arguments: \'name\' and \'value\'')
        if isinstance(value, str) and len(value) == 0:
            raise TypeError('integer_validator() missing 1 required \
positional argument: \'value\'')
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
