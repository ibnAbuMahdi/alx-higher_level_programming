#!/usr/bin/python3

def uppercase(s):
    for c in s:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            k = ord(c) - 32
        else:
            k = ord(c)
        print(chr(k), end="")
    print("")
