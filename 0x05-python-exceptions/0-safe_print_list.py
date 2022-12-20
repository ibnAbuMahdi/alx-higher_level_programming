#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0 
    try:
        while i < x:
            print(my_list[i], end="")
            i += 1
    except IndexError:
        print("", end="")
        # do nothing
    finally:
        if i > 0:
            print("")
    return (i)
