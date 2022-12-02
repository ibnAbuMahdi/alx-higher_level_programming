#!/usr/bin/python3
from calculate_1 import add, sub, div, mul
a = 10
b = 5
if __name__ == "__main__":
    print("{} + {} = {}".format(int(a), int(b), int(add(a, b))))
    print("{} - {} = {}".format(int(a), int(b), int(sub(a, b))))
    print("{} * {} = {}".format(int(a), int(b), int(mul(a, b))))
    print("{} / {} = {}".format(int(a), int(b), int(div(a, b))))
