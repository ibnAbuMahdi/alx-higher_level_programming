#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is not None:
        ln = len(my_list)
        if ln == 0:
            return None
        mx = int()
        for i in my_list:
            if i > mx:
                mx = i
        return mx
