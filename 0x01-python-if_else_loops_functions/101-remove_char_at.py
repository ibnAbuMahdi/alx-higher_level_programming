#!/usr/bin/python3

def remove_char_at(st, n):
    cp = []
    if type(n) is int and n >= 0:
        i = j = 0
        for c in st:
            if i is not n:
                cp.append(st[i])
                j += 1
            i += 1
    else:
        return st
    s = ""
    for c in cp:
        s += c
    return s
