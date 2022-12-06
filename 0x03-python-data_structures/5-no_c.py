#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for alp in my_string:
        if alp != 'c' and alp != 'C':
            new_str += alp
    return new_str
