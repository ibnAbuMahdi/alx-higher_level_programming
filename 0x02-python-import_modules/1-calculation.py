#!/usr/bin/python3
from calculate_1 import add
from calculate_1 import sub
from calculate_1 import div
from calculate_1 import mul
a = 1
b = 2
if __name__ == "__main__":
    print("{} + {} = {}".format(int(a), int(b), int(add(a, b))))
    print("{} - {} = {}".format(int(a), int(b), int(sub(a, b))))
    print("{} * {} = {}".format(int(a), int(b), int(mul(a, b))))
    print("{} / {} = {}".format(int(a), int(b), int(div(a, b))))
