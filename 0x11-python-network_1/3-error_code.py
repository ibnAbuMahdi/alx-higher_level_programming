#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status """
import urllib.request
import urllib.parse
import urllib.error
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as resp:
            page = resp.read()
            print(page.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
