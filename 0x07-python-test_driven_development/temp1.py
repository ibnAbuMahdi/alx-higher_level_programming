#!/usr/bin/python3
""" 2-matrix_divided.py """

matrix_divided = __import__('2-matrix_divided').matrix_divided


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/2-matrix_divided.txt')
