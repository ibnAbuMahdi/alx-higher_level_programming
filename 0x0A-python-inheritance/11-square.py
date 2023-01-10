#!/usr/bin/python3
""" 9-rectangle.py """


class BaseGeometry:
    """ Base Geometry """

    def area(self):
        """area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ int val """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):

    """ Rectangle class that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ init """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ string version of rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """ Square class that inherits from Rectangle """

    def __init__(self, size):
        """ init """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ returns the area of the square """
        return self.__size * self.__size

    def __str__(self):
        """ string version of square """
        return "[Square] {}/{}".format(self.__size, self.__size)
