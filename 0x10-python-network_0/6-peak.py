#!/usr/bin/python3
""" find a peak in a list """


def find_peak(ls):
    """ find the peak """
    h = len(ls)
    m = int((h - 0)/2)
    if h == 0:
        return None
    return f_peak(ls, 0, m, h)


def f_peak(ls, lo, m, h):
    """ fpeak find the peak """
    if m == 0 or (m == h - 1 and m != 1):
        return ls[m]
    if ls[m-1] > ls[m]:
        h = m
        m = lo + int((h - lo)/2)
        return f_peak(ls, lo, m, h)
    elif m + 1 < h and (ls[m+1] > ls[m]
                        or (ls[m-1] == ls[m] and
                            ls[m+1] == ls[m] and m < h-2)):
        low = m
        m = low + int((h - low)/2)
        return f_peak(ls, low, m, h)
    else:
        return ls[m]
