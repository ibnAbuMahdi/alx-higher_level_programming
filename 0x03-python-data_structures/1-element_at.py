#!/usr/bin/python3
def element_at(my_list, idx):
    if isinstance(idx, int):
        if (idx < 0):
            return None
        ln = len(my_list)
        if idx > ln - 1:
            return None
        return my_list[idx]
    return None
