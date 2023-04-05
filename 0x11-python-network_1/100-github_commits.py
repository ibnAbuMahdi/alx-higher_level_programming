#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status """
import requests
from sys import argv as args

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"
    data = requests.get(url.format(args[1], args[2]))
    cmts = data.json()
    for cmt in list(data.json())[:10]:
        print("{}: {}".format(cmt.get('sha'),
                              cmt.get('commit').get('author').get('name')))
