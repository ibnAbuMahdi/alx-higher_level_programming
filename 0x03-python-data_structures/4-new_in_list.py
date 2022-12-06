#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if isinstance(idx, int):
        new_list = []
        new_list.extend(my_list)
        if (idx < 0):
            return new_list
        ln = len(my_list)
        if idx > ln - 1:
            return new_list
        new_list[idx] = element
        return new_list
    return None
