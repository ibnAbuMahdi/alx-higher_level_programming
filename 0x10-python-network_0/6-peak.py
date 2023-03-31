#!/usr/bin/python3
""" find a peak in a list """

def find_peak(ls):
    """ find the peak """
    l = 0
    h = len(ls)
    m = int((h - l)/2)
    if h == 0:
        return None
    f_peak(ls, l, m, h)

def f_peak(ls, l, m, h):
    """ fpeak find the peak """
    if m == 0 or m == h - 1:
        return ls[m]
    if ls[m-1] > ls[m]:
        h = m
        m = l + int((h - l)/2)
         
        f_peak(ls, l, m, h)
    elif ls[m+1] > ls[m]:
        l = m
        m = l + int((h - l)/2)
        f_peak(ls, l, m, h)
    else:
        print(m)
        exit

