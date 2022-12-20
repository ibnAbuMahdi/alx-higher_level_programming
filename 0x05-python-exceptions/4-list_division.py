#!/usr/bin/python3

def list_division(l1, l2, x=0):
    i = res = 0
    lo = []
    while i < x:
        try:
            res = l1[i] / l2[i]
            i += 1
        except TypeError:
           i += 1
           print("wrong type")
           res = 0
        except ZeroDivisionError:
            i += 1
            print("division by 0")
            res = 0
        except IndexError:
            i += 1
            res = 0
            print("out of range")
        finally:
            lo.append(res)

    return lo
