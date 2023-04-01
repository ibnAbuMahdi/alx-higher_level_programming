#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status """
import urllib.request
from sys import argv


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as resp:
        info = resp.info()
    print(info['X-Request-Id'])
