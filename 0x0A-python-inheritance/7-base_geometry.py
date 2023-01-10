#!/usr/bin/python3
""" 6-base_geometry.py """


class BaseGeometry:
    """ Base Geometry """

    def area(self):
        """ area """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ int val """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
