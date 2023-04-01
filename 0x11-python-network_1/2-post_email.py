#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status """
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as resp:
        page = resp.read()
    print(page.decode('utf-8'))
