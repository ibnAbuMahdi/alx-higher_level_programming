#!/usr/bin/python3
""" 2-matrix_divided.py """


def matrix_divided(mat, div):
    """ divide matrix mat by div """

    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if type(mat) is not list:
        raise TypeError('matrix must be a matrix (list of lists)\
of integers/floats')

    size = -1
    nList = []
    for row in mat:
        if type(row) is not list:
            raise TypeError('matrix must be a matrix (list of \
lists) of integers/floats')

        if (size != -1 and size != len(row)):
            raise TypeError('Each row of the matrix must have the same size')
        else:
            size = len(row)

        nrow = []
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError('matrix must be a matrix (list \
of lists) of integers/floats')
            nrow.append(round(i / div, 2))

        nList.append(nrow)
    return nList
