#!/usr/bin/python3
def only_diff_elements(set1, set2):
    return (set1.difference(set2)).union(set2.difference(set1))