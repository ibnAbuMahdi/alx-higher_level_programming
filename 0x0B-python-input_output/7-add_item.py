#!/usr/bin/python3
""" 7-add_item.py """
import json
import os
from sys import argv
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

ln = 0
fname = "add_item.json"
nlist = []
if len(argv) > 1:
    nlist = list(argv[1:])

if os.path.exists(fname):
    ls = load_from_json(fname)
    ls.extend(nlist)
    nlist = ls[:]
save_to_json(nlist, fname)
