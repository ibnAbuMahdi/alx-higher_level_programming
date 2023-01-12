#!/usr/bin/python3
""" 101-stats.py """
import sys


codes = {200: 0, 301: 0, 400: 0, 403: 0, 404: 0, 405: 0, 500: 0}
size = [0]
cnt = 0


def parse_line(line, codes={}, size=[0]):
    """ parse the line """
    items = line.split()
    size[0] += int(items[-1])
    if int(items[-2]) in codes:
        codes[int(items[-2])] += 1


def print_stat(size, codes):
    """ print the line """
    print("File size:", size[0])
    for key, val in codes.items():
        if val > 0:
            print("{}: {}".format(key, val))


try:
    for line in sys.stdin:
        parse_line(line, codes, size)
        cnt += 1
        if cnt > 0 and cnt % 10 == 0:
            print_stat(size, codes)
except KeyboardInterrupt as interrupt:
    print_stat(size, codes)
