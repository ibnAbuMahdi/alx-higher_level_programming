#!/usr/bin/python3

text_indent = __import__('5-text_indentation').text_indentation


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/5-text_indentation.txt')
