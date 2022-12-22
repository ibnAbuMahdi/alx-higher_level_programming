#!/usr/bin/python3

def print_last_digit(num):
    if num < 0:
        rem = (-1 * num) % 10
    else:
        rem = num % 10
    print(rem, end="")
    return rem
