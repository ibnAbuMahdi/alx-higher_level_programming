#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status """
import requests
from sys import argv as args

if __name__ == "__main__":
    headers = {"Accept": "application/vnd.github+json"}
    url = "https://api.github.com/repos/{}/{}/commits"
    data = requests.get(url.format(args[1], args[2]), headers=headers)
    cmts = data.json()
    cmts_dict = {}
    for cmt in cmts:
        cmts_dict[cmt['commit']['author']['date']] =\
                [cmt['sha'], cmt['commit']['author']['name']]
    cmts_keys = list(cmts_dict.keys())
    cmts_keys.sort(reverse=True)
    cmts_sorted = {i: cmts_dict[i] for i in cmts_keys}
    for k, v in cmts_sorted.items():
        print("{}: {}".format(v[0], v[1]))
