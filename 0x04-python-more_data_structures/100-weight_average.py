#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    prod = list(map(lambda t: (t[0] * t[1]), my_list))
    weight = list(map(lambda t: t[1], my_list))
    sum_prod = 0
    sum_weight = 0
    for i in prod:
        sum_prod += i
    for i in weight:
        sum_weight += i
    return sum_prod / sum_weight
