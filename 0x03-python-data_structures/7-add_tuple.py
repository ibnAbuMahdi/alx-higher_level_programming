#!/usr/bin/python3
def add_tuple(a=(), b=()):
    ta = None
    tb = None
    la = len(a)
    lb = len(b)
    if la == 0:
        ta = 0, 0
    elif la == 1:
        ta = a[0], 0
    else:
        ta = a[0], a[1]

    if lb == 0:
        tb = 0, 0
    elif lb == 1:
        tb = b[0], 0
    else:
        tb = b[0], b[1]
    t = ta[0] + tb[0], ta[1] + tb[1]
    return t

