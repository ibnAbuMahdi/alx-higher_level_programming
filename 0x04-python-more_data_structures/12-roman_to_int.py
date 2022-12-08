#!/usr/bin/python3
def roman_to_int(r_str):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500}
    if not isinstance(r_str, str) or r_str is None:
        return 0
    string = r_str.upper()
    num = 0
    ln = len(string)
    i = 0
    while i < ln:
        nm1 = dic.get(string[i])
        if i < ln - 1:
            nm2 = dic.get(string[i + 1])
            if nm1 < nm2:
                num += nm2 - nm1
                i += 1
            else:
                num += nm1
        else:
            num += nm1
        i += 1
    return num
