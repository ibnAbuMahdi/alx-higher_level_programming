#!/usr/bin/python3

say_name = __import__('3-say_my_name').say_my_name


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/3-say_my_name.txt')
