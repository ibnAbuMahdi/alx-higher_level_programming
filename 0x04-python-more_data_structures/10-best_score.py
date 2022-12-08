#!/usr/bin/python3
def best_score(a_d):
    if a_d is None:
        return None
    mx = None
    key = None
    for k, v in a_d.items():
        if mx is None:
            mx = v
            key = k
            continue
        if v > mx:
            mx = v
            key = k
    return key
