#!/usr/bin/python3

print_square = __import__('4-print_square').print_square


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/4-print_square.txt')
